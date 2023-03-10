#!/usr/bin/env python3
""" mod doc str """
import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ filter_datum doc str """
    pat = '(?P<nm>' + '=|'.join(fields) + '=)' + f'[^{separator}]+{separator}'
    return re.sub(pat, r"\g<nm>{}{}".format(redaction, separator), message)


def get_logger() -> logging.Logger:
    """ func doc str """
    logger = logging.getLogger("user_data")
    logger.propagate = False
    logger.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ returns a connection object to a mysql db """
    u_name = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    passwd = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db = os.environ.get("PERSONAL_DATA_DB_NAME")

    c = mysql.connector.connect(
            user=u_name,
            password=passwd,
            host=host,
            database=db
        )
    return c


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ func doc str """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
            )
        return super().format(record)


def main() -> None:
    """ main func """
    con = get_db()
    cursor = con.cursor()
    query = "SELECT * FROM users;"
    cursor.execute(query)
    keys = (
        'name', 'email', 'phone', 'ssn', 'password', 'ip',
        'last_login', 'user_agent'
    )
    logger = get_logger()
    for row in cursor:
        dct = {}
        i = 0
        for itm in keys:
            dct[itm] = row[i]
            i += 1
        str_ = ''
        for key in dct:
            str_ += key + '=' + str(dct[key]) + ';'
        # log_record = logging.LogRecord("user_data", logging.INFO,
        #                                None, None, str_, None, None)
        # formatter = RedactingFormatter(fields=list(keys)[:5])
        # print(formatter.format(log_record))
        logger.info(str_)
    cursor.close()
    con.close()


if __name__ == "__main__":
    main()

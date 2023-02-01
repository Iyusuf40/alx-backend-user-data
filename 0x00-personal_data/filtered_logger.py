#!/usr/bin/env python3
""" mod doc str """


import re


def filter_datum(fields, redaction, message, separator) -> str:
    """ filter_datum doc str """
    for f in fields:
        pattern = f"(.*{f}=)([^;]*)(.*)"
        message = re.sub(pattern, r"\1{}\3".format(redaction), message)
    return message

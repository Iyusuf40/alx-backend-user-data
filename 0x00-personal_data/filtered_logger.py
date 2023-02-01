#!/usr/bin/env python3
""" mod doc str """


import re


r = r"\1{}\3"


def filter_datum(fields, redaction, message, separator) -> str:
    """ filter_datum doc str """
    for f in fields:
        message = re.sub(f"(.*{f}=)([^;]*)(.*)", r.format(redaction), message)
    return message

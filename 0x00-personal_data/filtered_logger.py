#!/usr/bin/env python3
""" mod doc str """


import re


def filter_datum(fields, redaction, message, separator) -> str:
    """ filter_datum doc str """
    repl = r"\g<nm>{}".format(redaction)
    pat = '(?P<nm>' + '=|'.join(fields) + '=)' + '[^;]*'
    return re.sub(pat, repl, message)

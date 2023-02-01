#!/usr/bin/env python3
""" mod doc str """


import re


def filter_datum(fields, redaction, message, separator) -> str:
    """ filter_datum doc str """
    pat = '(?P<nm>' + '=|'.join(fields) + '=)' + f'[^{separator}]*'
    # assuming separator = ;
    # pat = '(?P<nm>password=|date_of_birth=)[^;]*'
    # ?P<nm> refers to the matched value of one of password=
    # or date_of_birth=
    # r"\g<nm>" substitutes the value of ?P<nm> in place
    return re.sub(pat, r"\g<nm>{}".format(redaction), message)

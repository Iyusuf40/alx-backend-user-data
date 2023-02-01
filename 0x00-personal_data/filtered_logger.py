#!/usr/bin/env python3
""" mod doc str """


import re
from typing import List


def filter_datum(fields: List, redaction: str,
                 message: str, separator: str) -> str:
    """ filter_datum doc str """
    pat = '(?P<nm>' + '=|'.join(fields) + '=)' + f'[^{separator}]+{separator}'
    return re.sub(pat, r"\g<nm>{}{}".format(redaction, separator), message)

#!/usr/bin/env python3
"""
Auth class defined here
"""
from flask import abort, request
from api.v1.auth.auth import Auth
from typing import Tuple
import base64
import io


class BasicAuth(Auth):
    """ BasicAuth class """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """doc str"""
        if not authorization_header:
            return None
        if type(authorization_header) != str:
            return None

        comp = authorization_header.split(' ')
        if comp[0] != 'Basic':
            return None

        return comp[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """decode wrapper func"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None

        try:
            res = base64.b64decode(
                bytes(base64_authorization_header, 'utf-8')
            )
            res = res.decode('utf-8')

        except Exception as e:
            # print(e)
            res = None

        return res

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """doc str"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':'))

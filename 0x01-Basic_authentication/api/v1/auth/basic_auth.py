#!/usr/bin/env python3
"""
Auth class defined here
"""
from flask import abort, request
from api.v1.auth.auth import Auth


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

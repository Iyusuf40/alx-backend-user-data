#!/usr/bin/env python3
"""
Auth class defined here
"""
from flask import abort, request
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class """

    pass

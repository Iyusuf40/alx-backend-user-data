#!/usr/bin/env python3
"""
SessionAuth class defined here
"""
from flask import abort, request
from api.v1.auth.auth import Auth
from typing import Tuple, TypeVar
# import base64
from models.user import User


class SessionAuth(Auth):
    """ BasicAuth class """

    pass

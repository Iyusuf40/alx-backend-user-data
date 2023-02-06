#!/usr/bin/env python3
"""
Auth class defined here
"""
from flask import abort, request
from typing import List, TypeVar
from models.user import User


class Auth:
    """ Auth class """

    def require_auth(
        self, path: str, excluded_paths: List[str]
    ) -> bool:
        """ determines if authentication is required """
        return False

    def authorization_header(self, request=None) -> str:
        """ doc str """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ doc str """
        return None

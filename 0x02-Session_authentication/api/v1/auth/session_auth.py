#!/usr/bin/env python3
"""
SessionAuth class defined here
"""
from flask import abort, request
from api.v1.auth.auth import Auth
from typing import Tuple, TypeVar
import uuid
from models.user import User


class SessionAuth(Auth):
    """ SessionAuth class """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a new session """
        if not user_id:
            return None
        if type(user_id) != str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

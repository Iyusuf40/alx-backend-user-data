#!/usr/bin/env python3
""" mod doc str """
from typing import List
import bcrypt


def hash_password(password: str) -> bytes:
    """ hashes passeord """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt(4))

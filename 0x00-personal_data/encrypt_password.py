#!/usr/bin/env python3
""" mod doc str """
from typing import List
import bcrypt


def hash_password(password: str) -> bytes:
    """ hashes passeord """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt(4))


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ checks if passwd is valid """
    return bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password)

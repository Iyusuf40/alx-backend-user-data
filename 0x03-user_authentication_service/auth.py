"""auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ returns a passwd hash """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt(4))

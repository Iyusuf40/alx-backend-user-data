"""auth module
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """ returns a passwd hash """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt(4))


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """func doc str"""
        user_exists = False
        try:
            existing_user = self._db.find_user_by(email=email)
            user_exists = True
        except Exception:
            pass
        if user_exists:
            raise ValueError(f"User {email} already exists")
        hashed_passwd = _hash_password(password)
        return self._db.add_user(email=email, hashed_password=hashed_passwd)

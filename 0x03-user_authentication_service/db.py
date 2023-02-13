#!/usr/bin/env python3
"""DB module
"""
import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import TypeVar, Type, Mapping
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        '''adds a User to db'''
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kw: Mapping) -> User:
        ''' searches for user by kw '''
        user = None
        query = self._session.query(User)
        searched = False
        for key in kw:
            if key == 'email':
                query = query.filter(
                            User.email == kw[key]
                            )
                searched = True
            elif key == 'id':
                query = query.filter(
                            User.id == kw[key]
                            )
                searched = True
            elif key == 'hashed_password':
                query = query.filter(
                            User.hashed_password == kw[key]
                            )
                searched = True
            elif key == 'session_id':
                query = query.filter(
                            User.session_id == kw[key]
                            )
                searched = True
            elif key == 'reset_token':
                query = query.filter(
                            User.reset_token == kw[key]
                            )
                searched = True
        all_users = query.all()
        if not all_users:
            raise NoResultFound
        if searched is False:
            raise InvalidRequestError
        return all_users[0]

    def update_user(self, user_id: int, **kw: Mapping) -> None:
        """ updates a user """
        valid_keys = ['email', 'id', 'hashed_password',
                      'session_id', 'reset_token']
        user = self.find_user_by(id=user_id)
        for key in kw:
            if key not in valid_keys:
                raise ValueError
            user.__setattr__(key, kw[key])
        self._session.commit()

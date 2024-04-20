#!/usr/bin/env python3
""" Auth module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class for the API
    """

    def __init__(self):
        """ Constructor of the Auth class
        """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth method that returns
        True if the path is not in the list
        """

        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        for exclude_path in excluded_paths:
            if path.strip("/") in exclude_path.strip("/"):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header method that returns None
        """
        if request is None or request.headers.get("Authorization") is None:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method that returns None
        """

        return request

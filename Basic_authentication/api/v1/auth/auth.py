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

        for path in excluded_paths:
            if path in path:
                return False
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header method that returns None
        """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method that returns None
        """
        return request

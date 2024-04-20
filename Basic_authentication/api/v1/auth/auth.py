#!/usr/bin/env python3
""" Auth module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class for the API
    """
    def __init__(self) -> None:
        """ Constructor of the Auth class
        """
        
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        return request

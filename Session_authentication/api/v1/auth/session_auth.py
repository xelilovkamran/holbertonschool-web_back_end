#!/usr/bin/env python3
""" Module of Session Authentication
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session Authentication Class inherited from Auth
    """

    def __init__(self):
        super().__init__()

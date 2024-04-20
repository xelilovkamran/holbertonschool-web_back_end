#!/usr/bin/env python3
""" BasicAuth module for the API
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def __init__(self):
        """ Constructor of the BasicAuth class
        """

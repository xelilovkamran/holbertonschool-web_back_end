#!/usr/bin/env python3
""" BasicAuth module for the API
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def __init__(self):
        """ Constructor of the BasicAuth class
        """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract_base64_authorization_header method that returns None
        """
        if (authorization_header is None or
            type(authorization_header) is not str or
                authorization_header.startswith("Basic ") is False):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ decode_base64_authorization_header method that returns None
        """
        if (base64_authorization_header is None or
                type(base64_authorization_header) is not str):
            return None

        try:
            base64_authorization_header = base64.b64decode(
                base64_authorization_header).decode("utf-8")
            return base64_authorization_header
        except Exception:
            return None
        return 'asd'

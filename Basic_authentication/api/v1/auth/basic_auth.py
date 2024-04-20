#!/usr/bin/env python3
""" BasicAuth module for the API
"""

from api.v1.auth.auth import Auth
from typing import Tuple
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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> Tuple[str, str]:
        """ extract_user_credentials method that returns None
        """
        if (decoded_base64_authorization_header is None or
                type(decoded_base64_authorization_header) is not str or
                ":" not in decoded_base64_authorization_header):
            return (None, None)

        return tuple(decoded_base64_authorization_header.split(":", 1))

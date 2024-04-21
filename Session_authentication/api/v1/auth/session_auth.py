#!/usr/bin/env python3
""" Module of Session Authentication
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session Authentication Class inherited from Auth
    """

    def __init__(self):
        self.user_id_by_session_id = {}
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """ Create a Session ID
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id: str = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

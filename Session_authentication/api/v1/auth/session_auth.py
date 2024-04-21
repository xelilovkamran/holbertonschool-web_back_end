#!/usr/bin/env python3
""" Module of Session Authentication
"""

from api.v1.auth.auth import Auth
from typing import Dict
import uuid


class SessionAuth(Auth):
    """ Session Authentication Class inherited from Auth
    """
    user_id_by_session_id: Dict = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a Session ID
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id: str = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Return a User ID based on a Session ID
        """
        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

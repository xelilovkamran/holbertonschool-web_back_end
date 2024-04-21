#!/usr/bin/env python3
""" Module of Session Expiration Authentication
"""

from flask import request
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime


class SessionExpAuth(SessionAuth):
    """ Session Expiration Authentication Class inherited from SessionAuth
    """

    def __init__(self):
        """ Constructor
        """
        super().__init__()
        self.session_duration = getenv("SESSION_DURATION", 0)

    def create_session(self, user_id=None):
        """ Create a Session ID
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.now()
        }

    def user_id_for_session_id(self, session_id=None):
        """ Return a User ID based on a Session ID
        """
        if session_id is None:
            return None

        if session_id not in self.user_id_by_session_id:
            return None

        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]["user_id"]

        if "created_at" not in self.user_id_by_session_id[session_id]:
            return None

        if ((datetime.now() - self.user_id_by_session_id
             [session_id]["created_at"]).seconds > self.session_duration):
            # del self.user_id_by_session_id[session_id]
            return None

        return self.user_id_by_session_id[session_id]["user_id"]

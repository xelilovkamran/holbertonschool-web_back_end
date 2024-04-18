#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a hashed password"""
    hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return hashed_pass

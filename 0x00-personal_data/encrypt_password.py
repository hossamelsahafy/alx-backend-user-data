#!/usr/bin/env python3
"""
    Encrypting passwords
"""

import bcrypt


def hash_password(password: str):
    """
        returns a salted, hashed password,
        which is a byte string.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
#!/usr/bin/env python3
"""
    Auth class
"""
from typing import List, TypeVar


class Auth():
    """Define Auth Class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False And Path """
        return False

    def authorization_header(self, request=None) -> str:
        """
             returns None - request
        """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Return None
        """
        return None

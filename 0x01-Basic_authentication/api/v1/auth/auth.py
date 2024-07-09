#!/usr/bin/env python3
"""
    Auth class
"""
from typing import List, TypeVar


class Auth():
    """Define Auth Class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False And Path """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for ex_path in excluded_paths:
            if path.rstrip('/') == ex_path.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        if request is None:
            return None
    
        auth_header = request.headers.get("Authorization")
    
        if auth_header is None:
            return None
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Return None
        """
        return None

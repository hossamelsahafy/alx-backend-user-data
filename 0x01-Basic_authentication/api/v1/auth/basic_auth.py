#!/usr/bin/env python3
""" Basic Auth """
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Define BasicAuth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
         returns the Base64 part of the
         Authorization header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(self,
                                           base64_auth_header: str) -> str:
        """
             returns the decoded value
             of a Base64 string base64_authorization_header
        """
        if base64_auth_header is None:
            return None
        if not isinstance(base64_auth_header, str):
            return None
        try:
            decode_byte = base64.b64decode(base64_auth_header,
                                           validate=True)
            return decode_byte.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

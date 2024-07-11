#!/usr/bin/env python3
"""Session Authentication Module"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """Define SessionDBAuth Class"""
    def __init__(self):
        """Initialize SessionDBAuth Class"""
        super().__init__()

    def create_session(self, user_id=None):
        """Create Session Method"""
        session_id = super().create_session(user_id)
        if session_id:
            user = UserSession(user_id, session_id=session_id)
            return session_id
        return None

    def user_id_for_session_id(self, session_id=None):
        """User ID for Session ID Method"""
        if session_id is None:
            return None
        user = UserSession.query.filter_by(session_id=session_id).first()
        if user:
            return user.user_id
        return None

    def destroy_session(self, request=None):
        """Destroy Session Method"""
        if request and 'session_id' in request.cookies:
            session_id = request.cookies.get('session_id')
            self.user_id_by_session_id(session_id, None)

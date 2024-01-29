import os
from social_core.backends.oauth import BaseOAuth2

class GoogleOAuth2(BaseOAuth2):
    name = 'google-oauth2'
    AUTHORIZATION_URL = 'https://accounts.google.com/o/oauth2/auth'
    ACCESS_TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'
    USER_DATA_URL = 'https://www.googleapis.com/oauth2/v1/userinfo'
    REDIRECT_STATE = False
    STATE_PARAMETER = False
    ACCESS_TOKEN_METHOD = 'POST'
    DEFAULT_SCOPE = ['profile', 'email']
    ID_KEY = 'id'

    def get_key_and_secret(self):
        """Return your Key and Secret."""
        return os.getenv('GOOGLE_CLIENT_ID'), os.getenv('GOOGLE_CLIENT_SECRET')
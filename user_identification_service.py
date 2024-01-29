from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from social_core.backends.google import GoogleOAuth2
from social_core.exceptions import AuthFailed
from models import User
import repository

def register_user(user: User):
    # Add the user to the MongoDB collection
    repository.add_user(user)

def user_login(form_data: OAuth2PasswordRequestForm):
    google_auth = GoogleOAuth2()
    try:
        user = google_auth.do_auth(form_data.username, form_data.password)
    except AuthFailed:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # If the user is authenticated, return a token
    return {"access_token": user.social_auth.get('access_token'), "token_type": "bearer"}
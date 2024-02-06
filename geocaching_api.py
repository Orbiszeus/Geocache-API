from fastapi import FastAPI, HTTPException, Security, WebSocket, Request ,Response, Body, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import repository
from models import Game, User
import game
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth, OAuthError
import json 
import os   
from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.config import Config
from starlette.responses import HTMLResponse, RedirectResponse
from dotenv import load_dotenv
import requests

app = FastAPI()

config = Config('.env')
oauth = OAuth(config)

load_dotenv()  

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URIS")
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
VUE_REDIRECT_URL = "http://localhost:5173/game_panel"
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)    
    
@app.post("/create_game", response_description="Create a new game object", status_code=201, response_model=Game)
def create_game(request: Request, response: Response, game: Game = Body(...)):
    repository.create_game(request, response, game)
    return 0


@app.get("/login")
async def login_google():
    return {
        "url": f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"
    }

@app.get("/auth")
async def auth_google(code: str):
    token_url = "https://accounts.google.com/o/oauth2/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get("access_token")
    user_info_response = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
    user_info = user_info_response.json()
    redirect_url = f"{VUE_REDIRECT_URL}?authenticated=true&user_info={user_info}"

    return RedirectResponse(url=redirect_url)

@app.post("/game_panel")
async def join_game():
    
    return game.get_panel_data()

@app.post("/create_game")
async def join_game():
    
    return game.create_game()
    

@app.post("/join_game")
async def join_game():
    return game.play_game()




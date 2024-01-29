from fastapi import FastAPI, HTTPException, Security, WebSocket, Request ,Response, Body, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import repository
from models import Game, User
import game
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import user_identification_service

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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

@app.post("/register")
async def register_user(user: User):
    return user_identification_service.register_user(user)

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return user_identification_service.user_login(form_data)

@app.post("/join_game")
async def join_game():
    return game.play_game()


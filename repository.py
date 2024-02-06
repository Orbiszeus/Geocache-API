from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
import models 
from pymongo import MongoClient
import json

def __init__(self, uri: str, db_name: str, collection_name: str):
     self.client = MongoClient(uri)
     self.db = self.client[db_name]
     self.collection = self.db[collection_name]
        
def create_game(self, request, response, game: models.Game):
     game_dict = jsonable_encoder(game)
     new_game = self.collection.insert_one(game_dict)
     # created_game = self.collection.find_one({"_id": new_game.inserted_id})
     return game.create_game_server(game)

def add_user(self, user: models.User):
     user_dict = user.dict()
     self.collection.insert_one(user_dict)
     return user_dict

def get_all_games() -> List[models.Game]:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['your_database_name']  # replace with your database name
    games_collection = db['games']

    games = []
    for game in games_collection.find():
        games.append(models.Game(
            GameID=game['GameID'],
            OrganizerID=game['OrganizerID'],
            GameArea=game['GameArea'],
            Status=game['Status'],
            WinnerID=game.get('WinnerID')  # use get in case WinnerID is not present
        ))

    return games
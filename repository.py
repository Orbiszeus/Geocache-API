
from fastapi.encoders import jsonable_encoder
from typing import List
import models 
from pymongo.server_api import ServerApi

from pymongo import MongoClient


class Repository:
     uri = "mongodb+srv://baris_ozdizdar:ZhcyQqCIwQMS8M29@geocachedb.63lwf9c.mongodb.net/?retryWrites=true&w=majority"

     client = MongoClient(uri, server_api=ServerApi('1'))

     db = client['GeocacheDB']  
     
     def __init__(self):
        # Initialize your collections in the constructor
        self.user_collection = self.db['User']
        self.participation_collection = self.db['Participation']
        self.image_storage_collection = self.db['ImageStorage']
        self.game_collection = self.db['Game']
        self.cache_discovery_collection = self.db['CacheDiscovery']
        self.cache_collection = self.db['Cache']
          
     def create_game(request, response, game: models.Game):
          game_dict = jsonable_encoder(game)
          new_game = Repository.game.insert_one(game_dict)
          created_game = Repository.game_collection.find_one({"_id": new_game.inserted_id})
          return game.create_game_server(game)

     def add_user(self, user: models.User):
          try:
               user_dict = jsonable_encoder(user)
               self.user_collection.insert_one(user_dict)
               return user
          except Exception as e:
               print(e)
               return None
          
     def check_user(self, user_email) -> bool:
          try:
               user = self.user_collection.find_one({"Email": user_email})
               return user is not None
          except Exception as e:
               print(e)
               return False
          
     def get_panel_data(self) -> List[models.Game]:
        try:
            # Retrieve all documents from the 'Game' collection
            games_cursor = self.game_collection.find({})
            
            # Convert cursor to a list of Game models
            games_list = [models.Game(**game) for game in games_cursor]
            
            return games_list
        except Exception as e:
            print(e)
            return []
               
          

          

from typing import List, Optional
from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from pydantic.networks import AnyUrl
        
class User(BaseModel):
    
    UserID: str
    Name: str
    Email: str
    OAuthToken: str
    UserType: str
    
class GameArea(BaseModel):
    coordinates: List[List[float]]
    
class Location(BaseModel):
    type: str
    coordinates: List[float]
    
class Game(BaseModel):
    
    CacheID : str
    GameID: str
    OrganizerID: int
    GameArea:  GameArea
    Status: str
    WinnerID: Optional[int]
    
    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }
        arbitrary_types_allowed = True

class Cache(BaseModel):
    CacheID: int
    GameID: int
    Location: Location  
    Hint: str
    FoundByUserID: Optional[int]

class Participation(BaseModel):
    ParticipationID: str
    UserID: str
    GameID: int
    JoinedDate: str  

class CacheDiscovery(BaseModel):
    DiscoveryID: int
    CacheID: int
    UserID: int
    DiscoveryDate: str 
    ProofImage: str

class ImageStorage(BaseModel):
    ImageID: int
    RelatedID: int
    ImagePath: str
    ImageType: str

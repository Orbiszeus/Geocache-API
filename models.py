from typing import List, Optional
from pydantic import BaseModel

class BaseClass(BaseModel):
    class Config:
        orm_mode = True

class User(BaseClass):
    UserID: int
    Name: str
    Email: str
    OAuthToken: str
    UserType: str

class Game(BaseClass):
    GameID: int
    OrganizerID: int
    GameArea: str  
    Status: str
    WinnerID: Optional[int]

class Cache(BaseClass):
    CacheID: int
    GameID: int
    Location: str  
    Hint: str
    FoundByUserID: Optional[int]

class Participation(BaseClass):
    ParticipationID: int
    UserID: int
    GameID: int
    JoinedDate: str  

class CacheDiscovery(BaseClass):
    DiscoveryID: int
    CacheID: int
    UserID: int
    DiscoveryDate: str 
    ProofImage: str

class ImageStorage(BaseClass):
    ImageID: int
    RelatedID: int
    ImagePath: str
    ImageType: str

from pydantic import BaseModel
from typing import List

class UserInput(BaseModel):
    description: str
    interests: List[str]

class RecommendationResponse(BaseModel):
    topics: List[str]from pydantic import BaseModel
from typing import List

class UserInput(BaseModel):
    description: str
    interests: List[str]

class RecommendationResponse(BaseModel):
    topics: List[str]

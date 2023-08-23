from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str
    password: str
    email:str
    

class User (UserBase):
    id: int
    updated_at: datetime
    created_at: datetime

class UserCreate(UserBase):
    pass


class UserUpdate (UserBase):
    pass

class UserSign (BaseModel):
    username: str
    password: str


class TweetBase(BaseModel):
    content: str
    user: int

class Tweet (TweetBase):
    idTweet: int
    updated_at: datetime
    created_at: datetime

class TweetCreate(TweetBase):
    pass

class TweetUpdate(BaseModel):
    content: str
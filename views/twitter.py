from fastapi import APIRouter, HTTPException, Request, Body, Depends
from models.twitter import User, Tweet
from schemas.twitter import User as UserSchema, UserUpdate, UserCreate, UserSign, Tweet as TweetSchema, TweetCreate, TweetUpdate

from typing import List, Optional
from auth.auth_handler import signJWT
import logging
from auth.auth_bearer import JWTBearer

user_views = APIRouter()


@user_views.post("/users", response_model=UserSchema)
async def user_create(user_create: UserCreate):
    user = await User.create(
        username=user_create.username,
        password=user_create.password,
        email=user_create.email
    )
    return user

@user_views.post("/users/signup")
async def sign_user(user_sign: UserSign):
    logging.debug(user_sign.username)
    username_sign: Optional[User] = await User.get_or_none(username=user_sign.username)  
    password_sign: Optional[User] = await User.get_or_none(password=user_sign.password)
    if not username_sign :
        raise HTTPException(status_code=404, detail="user not found")
    elif not password_sign:
        raise HTTPException(status_code=404, detail="user not found")
    else:
        return signJWT(username_sign.email)



@user_views.get("/api/users", response_model=List[UserSchema])
async def user_list():
    users = await User.all().order_by('created_at')

    return users

@user_views.put("/users/{user_id}", response_model=UserSchema)
async def user_put(user_id: int, user_update: UserUpdate ):
    user: Optional[User] = await User.get_or_none(id=user_id)

    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    user.username = user_update.username
    user.password = user_update.password
    await user.save()
    return user


@user_views.delete("/users/{user_id}", response_model=UserSchema)
async def user_delete(user_id: int ):
    user: Optional[User] = await User.get_or_none(id=user_id)

    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    await user.delete()
    return user


@user_views.get("/home", dependencies=[Depends(JWTBearer())])
async def home_page(user_sign: UserSign) -> dict:
    user_sign: Optional[User] = await User.get_or_none(username=user_sign.username)   
    if not user_sign:
        raise HTTPException(status_code=404, detail="user not found")
    else:
        return {"data": "post added."}


@user_views.post("/users/tweet", dependencies=[Depends(JWTBearer())])
async def tweet_create(tweet_create: TweetCreate):
    try:
        user = await User.get(id=tweet_create.user)
        tweet = await Tweet.create(
            content=tweet_create.content,
            user=user
        )
        tweet_dict = dict(tweet)
        return tweet_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
@user_views.get("/users/tweet", dependencies=[Depends(JWTBearer())])
async def tweet_list():
    tweet = await Tweet.all().order_by('created_at')
    return tweet


@user_views.put("/users/tweet/{tweet_id}", dependencies=[Depends(JWTBearer())])
async def tweet_put(tweet_id: int, tweet_update: TweetUpdate ):
    tweet: Optional[Tweet] = await Tweet.get_or_none(idTweet=tweet_id)

    if not tweet:
        raise HTTPException(status_code=404, detail="tweet not found")
    tweet.content = tweet_update.content
    await tweet.save()
    return tweet

@user_views.delete("/users/tweet/{tweet_id}", dependencies=[Depends(JWTBearer())])
async def tweet_delete(tweet_id: int ):
    tweet: Optional[Tweet] = await Tweet.get_or_none(idTweet=tweet_id)

    if not tweet:
        raise HTTPException(status_code=404, detail="tweet not found")
    await tweet.delete()
    return tweet

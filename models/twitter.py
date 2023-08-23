from tortoise import fields
from tortoise.models import Model
from datetime import datetime


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.TextField()
    password = fields.TextField()
    email = fields.TextField()


    created_at = fields.DateField(default=datetime.utcnow)
    updated_at = fields.DateField(default=datetime.utcnow)


class Tweet(Model):
    idTweet = fields.IntField(pk=True)
    content = fields.TextField()
    user = fields.ForeignKeyField('models.User',related_name='tweets', null=False)


    created_at = fields.DateField(default=datetime.utcnow)
    updated_at = fields.DateField(default=datetime.utcnow)

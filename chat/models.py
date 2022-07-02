from django.db import models

from common.models import BaseModel


class Chat(BaseModel):
    # users = models.ManyToManyField(User)
    name = models.CharField(max_length=255)


class Message(BaseModel):
    chat = models.ForeignKey(Chat)
    # user = models.ForeignKey(User)
    text = models.TextField()

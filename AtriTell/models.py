from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.utils import timezone


class User(AbstractUser):
    tg_auth_token = models.CharField(max_length=15, null=True, unique=True)
    tg_user_id = models.BigIntegerField(null=True, unique=True)


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    
    random_url_id = models.UUIDField(default=uuid4)


class TgChannel(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    tg_user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='tg_user_id')

from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    
    random_url_id = models.UUIDField(default=uuid4)

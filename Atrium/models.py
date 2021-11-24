from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.CharField(max_length=30)
    creation_date = models.DateField(auto_now_add=True)
    # Add a unique link field here


class Note(models.Model):
    pass

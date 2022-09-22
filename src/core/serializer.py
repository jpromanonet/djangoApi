from sqlite3 import Timestamp
from unittest.util import _MAX_LENGTH
from rest_framework import serializer
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
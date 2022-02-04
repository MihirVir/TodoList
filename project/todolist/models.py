from time import time
from tkinter import CASCADE

from click import edit
from django.db import models
from django.contrib.auth.models import User
from enum import unique

import uuid

from django.forms import PasswordInput
from sqlalchemy import null
# Create your models here.

class Task(models.Model):
    taskId = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    taskName = models.CharField(max_length=50, blank=False, null = False)
    created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default = User)
    def __str__(self):
        return self.taskName
    

# class UserDb(models.Model):
#     username = models.CharField(max_length = 50, unique=True, null=False, blank=False)
#     password = models.CharField(max_length = 50, unique=True, null=False, blank=False)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, unique=True, editable=False)

#     def __str__(self):
#         return self.username

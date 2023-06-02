from django.db import models
from common.models import BaseModel
from type.models import Type
from django.contrib.auth.models import AbstractUser

class User(BaseModel, AbstractUser):

    def __str__(self):
        return self.username

class Account(BaseModel):
    accountName = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="accounts")

    def __str__(self):
        return self.accountName
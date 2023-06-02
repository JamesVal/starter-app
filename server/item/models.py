from django.db import models
from common.models import BaseModel
from user.models import Account
from type.models import Type

# Create your models here.

class Item(BaseModel):
    itemName = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True, related_name="items")

    def __str__(self):
        return self.itemName
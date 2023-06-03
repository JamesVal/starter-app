from django.db import models
from common.models import BaseModel
from user.models import Account
from item.models import Item

# Create your models here.

class Comment(BaseModel):
    content = models.TextField(blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True, related_name="comments")
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True, related_name="comments")

    def __str__(self):
        return self.content
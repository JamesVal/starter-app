from django.db import models
from common.models import BaseModel

class Type(BaseModel):
    typeName = models.CharField(max_length=255, unique=True)
    typeDescription = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.typeName

from django.db import models
from common.models import BaseModel

class TypeCategory(BaseModel):
    categoryName = models.CharField(max_length=255, unique=True)
    categoryDescription = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Type Categories"

    def __str__(self):
        return self.categoryName

class Type(BaseModel):
    typeName = models.CharField(max_length=255, unique=True)
    typeDescription = models.TextField(blank=True, null=True)
    category = models.ForeignKey(TypeCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.typeName

from django.db import models
from django.utils import timezone
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    # owner = models.ForeignKey(
    #     'settings.AUTH_USER_MODEL',
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name='owner+'
    # )

    class Meta:
        abstract = True
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.indexes import GinIndex
from django.conf import settings
from django.utils import timezone



class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    class Meta:
        db_table = 'cake_user'

        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['username']),
        ]

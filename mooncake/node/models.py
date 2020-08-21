from django.db import models
from django.utils import timezone
from django.contrib import admin
from tinymce.models import HTMLField


PUBLIC = 'public'
DRAFT = 'draft'
STATUSES = (
        (PUBLIC, 'public'),
        (DRAFT, 'draft'),
    )


class Node(models.Model):
    title = models.CharField(max_length=255)
    # content = models.TextField()
    content = HTMLField()
    source_url = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUSES, default=DRAFT)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    class Meta:
        db_table = 'cake_node'

from django.db import models
from django.utils import timezone


class Node(models.Model):
    PUBLIC = 'public'
    DRAFT = 'draft'
    STATUSES = (
        (PUBLIC, 'public'),
        (DRAFT, 'draft'),
    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    source_url = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUSES, default=DRAFT)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    class Meta:
        db_table = 'cake_node'

from django.db import models
from django.utils import timezone
from django.contrib import admin
from tinymce.models import HTMLField


class NodeType(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default='', blank=True, null=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cake_node_type'



class Node(models.Model):
    PUBLIC = 'public'
    DRAFT = 'draft'
    STATUSES = (
            (PUBLIC, 'public'),
            (DRAFT, 'draft'),
        )

    node_type = models.ForeignKey(NodeType, on_delete=models.CASCADE, related_name='nodes', default='')
    title = models.CharField(max_length=255)
    # content = models.TextField()
    content = HTMLField()
    source_url = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUSES, default=DRAFT)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    class Meta:
        db_table = 'cake_node'

        indexes = [
            models.Index(fields=['node_type']),
        ]

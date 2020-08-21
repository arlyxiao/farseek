from django.contrib import admin
from node.models import Node


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at',)
    pass

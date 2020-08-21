from django.contrib import admin
from django.forms import ModelChoiceField

from node.models import Node, NodeType


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'node_type', 'status', 'created_at', 'updated_at',)
    pass


@admin.register(NodeType)
class NodeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at', 'updated_at',)
    pass

from node.models import Node
from rest_framework import serializers


class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = ['title', 'content', 'source_url', 'created_at']

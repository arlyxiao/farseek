# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from node.models import Node
from node.serializers import NodeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all().order_by('-created_at')
    serializer_class = NodeSerializer
    permission_classes = [permissions.IsAuthenticated]

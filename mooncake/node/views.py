# from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions

from node.models import Node
from node.serializers import NodeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all().order_by('-created_at')
    serializer_class = NodeSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    return render(request, 'index.html', {})

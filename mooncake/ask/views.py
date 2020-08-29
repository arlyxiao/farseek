# from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions



def index(request):
    return render(request, 'ask/index.html', {})

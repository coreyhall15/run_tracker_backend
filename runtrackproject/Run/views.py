

# Create your views here.
from django.shortcuts import render
from .models import Run
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RunSerializer
# Create your views here.

class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    permission_classes = [permissions.AllowAny]
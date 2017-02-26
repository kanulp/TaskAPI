from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .Serializers import TestSerializers

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all().order_by('-date_created') 
	serializer_class = TestSerializers
	
from .models import Task
from .serializers import TaskSerializer

from rest_framework import generics
from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

class TaskList(generics.ListCreateAPIView):
    """
    Lists and creates tasks.
    """
    queryset = Task.objects.all()[:10]
    serializer_class = TaskSerializer

'''
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single Task and allows updates and deletion of a Task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'task_id'
'''

class TaskDetail(APIView):
    """
    Returns a single project.
    """
    def get_object(self, project_number):
        try:
            return Task.objects.get(pk=project_number)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, project_number, format=None):
        project = self.get_object(project_number)
        serializer = TaskSerializer(project)
        return Response(serializer.data) 


class TaskByCountry(APIView):
    """
    Returns projects by a country.
    """
    def get_object(self, country):
        try:
            return Task.objects.filter(country=country)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, country, format=None):
        projects = self.get_object(country)
        serializer = TaskSerializer(projects, many=True)
        return Response(serializer.data)
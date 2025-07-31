from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task

@api_view(['GET'])
def api_overview_function(request):
    api_urls = {
        'List': '/task_list_path/',
        'Detail View': '/task_detail_path/<str:pk>/',
        'Create': '/task_create_path/',
        'Update': '/task_update_path/<str:pk>/',
        'Delete': '/task_delete_path/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def task_list_function(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail_function(request, pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create_function(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def task_update_function(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance = task, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def task_delete_function(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Item successfully deleted !")






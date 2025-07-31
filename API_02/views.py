from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer

from .models import Post

@api_view(['GET'])
def api_overview_function(request):
    api_urls = {
        'List': '/post_list_path/',
        'Detail View': '/post_detail_path/<str:pk>/',
        'Create': '/post_create_path/',
        'Update': '/post_update_path/<str:pk>/',
        'Delete': '/post_delete_path/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def post_list_function(request):
    posts = Post.objects.all().order_by('-id')
    serializer = PostSerializer(posts, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def post_detail_function(request, pk):
    posts = Post.objects.get(id = pk)
    serializer = PostSerializer(posts, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def post_create_function(request):
    serializer = PostSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def post_update_function(request, pk):
    post = Post.objects.get(id = pk)
    serializer = PostSerializer(instance = post, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def post_delete_function(request, pk):
    post = Post.objects.get(id = pk)
    post.delete()
    return Response("Item successfully deleted !")

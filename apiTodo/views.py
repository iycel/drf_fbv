from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo

# Function Based Views
from rest_framework.decorators import api_view

def home(request):
    return HttpResponse('<center><h1 style="background-image: linear-gradient(90deg, blue, turquoise); padding:10px;">Welcome to ApiTodo</h1></center>')

@api_view(['GET'])
def todoList(request):
    queryset = Todo.objects.all()

    serializer = TodoSerializer(queryset, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def todoListCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
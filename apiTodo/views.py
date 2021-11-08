from django.http.response import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('<center><h1 style="background-image: linear-gradient(90deg, blue, turquoise); padding:10px;">Welcome to ApiTodo</h1></center>')

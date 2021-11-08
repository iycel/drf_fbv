from django.urls import path
from .views import home, todoList

urlpatterns = [
    path('', home),
    path('todolist/', todoList, name='todolist'),
]
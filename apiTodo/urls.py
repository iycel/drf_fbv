from django.urls import path
from .views import home, todoList, todoListCreate

urlpatterns = [
    path('', home),
    path('todolist/', todoList, name='todolist'),
    path('todolistcreate/', todoListCreate, name='todolistcreate'),
]
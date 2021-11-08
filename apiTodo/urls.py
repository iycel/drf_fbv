from django.urls import path
# from .views import todoList, todoListCreate
from .views import home, toDo_list

urlpatterns = [
    path('', home),
    # path('todolist/', todoList, name='todolist'),
    # path('todolistcreate/', todoListCreate, name='todolistcreate'),
    path('todolist/', toDo_list),
]
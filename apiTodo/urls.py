from django.urls import path
# from .views import todoList, todoListCreate, todoListUpdate, todoListDelete
from .views import home, toDo_Details, toDo_list

urlpatterns = [
    path('', home),
    # path('todolist/', todoList, name='todolist'),
    # path('todolistcreate/', todoListCreate, name='todolistcreate'),
    path('todolist/', toDo_list),
    # path('todolistupdate/<int:pk>', todoListUpdate),
    # path('todolistdelete/<int:pk>', todoListDelete),
    path('tododetails/<int:pk>', toDo_Details),
]
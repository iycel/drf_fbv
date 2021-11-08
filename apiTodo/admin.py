from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'task',
        'description',
        'priority',
        'done',
        'update',
        'createdDate'
    ]

admin.site.register(Todo, TodoAdmin)

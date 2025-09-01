from django.contrib import admin
from .models import NewTodo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)  

admin.site.register(NewTodo, TodoAdmin)
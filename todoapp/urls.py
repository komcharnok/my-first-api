from django.urls import path
from . import views_get

urlpatterns = [
    path('todo-list', views_get.get_all_todo),
]

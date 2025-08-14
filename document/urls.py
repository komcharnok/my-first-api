from django.urls import path
from . import views_get

urlpatterns = [
    path('doc-list', views_get.get_all_doc),
    path('doc-list-id/<int:id>', views_get.get_by_id_doc),  
]

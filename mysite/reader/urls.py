# reader/urls.py

from django.urls import path
from . import views

app_name = 'ktr_reader'

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('show/<int:pk>/', views.show_file, name='show_file'),
    path('diagram/<int:pk>/', views.diagram, name='diagram'),
]

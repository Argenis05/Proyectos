from django.urls import path, re_path
from .views import homee, procesamiento



urlpatterns = [
    path("miempresa/",homee, name="home"),
    path('procesamiento/<str:pk>/',procesamiento,name='procesamiento')
]
from django.urls import path, re_path
from .views import homee



urlpatterns = [
    path("miempresa/",homee, name="home"),
    #path('procesamiento/',procesamiento,name='procesamiento')
]
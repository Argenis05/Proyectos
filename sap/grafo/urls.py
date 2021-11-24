from django.urls import path, re_path
from .views import graf
app_name = "grafo"
urlpatterns = [

path("grafo/",graf, name="grafo")
    
]
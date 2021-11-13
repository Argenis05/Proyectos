from django.urls import path, re_path
from .views import about

app_name = "about"

urlpatterns = [
    path("aboutt/",about, name="about")
    
]
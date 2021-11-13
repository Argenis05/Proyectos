from django.urls import path, re_path
from .views import principal

app_name = "sintactico"

urlpatterns = [
    path("estru/",principal, name="patrones")
    
]
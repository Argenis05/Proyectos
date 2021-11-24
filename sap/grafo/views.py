from django.http.response import HttpResponse
from django.shortcuts import render
import math

def graf(request):
    template_name="grafo/grafo.html"
    return render(request, template_name, )
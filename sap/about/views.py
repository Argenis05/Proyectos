#from django.http.response import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def about (request):
    
    resultado=mifuncion(request)
    template_name='about/about.html'
    return render(request,template_name,{"nombreusuario":resultado,'edad':45})


def mifuncion(args):
    return 'Argenis'
""" 
    textHTML=
    <h1>hola mundo  </h1>
    
    <ul>
        <li> Donde
        <li> La fieta
    </ul>
   
    return HttpResponse(textHTML) 
"""
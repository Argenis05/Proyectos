from django.shortcuts import render
from .models import tessiu


def homee(request):
    Lista=tessiu.objects.get_queryset()
    L1,L2=procesaLista(Lista)
    milistas=[Lista,L1,L2]
    template_name="home/home.html"
    diccio= {'l':Lista,"otra":"informacion","Lista1":L1,"Lista2":L2,"mislistas":milistas}
    return render(request, template_name,diccio)

def procesaLista(L):
    listaColorMayor20=[]
    listaColorMenor20=[]
    for i in L:
        if i.color>20:
            listaColorMayor20.append(i)
        else:
            listaColorMenor20.append(i)
    return listaColorMayor20, listaColorMenor20

from django.shortcuts import render
from .models import tessiu
import math

def homee(request):
    Lista=tessiu.objects.get_queryset()
    L1,L2=procesaLista(Lista)
    distancias=euclidea(Lista)
    milistas=[Lista,L1,L2]
    template_name="home/home.html"
    diccio= {'l':Lista,"otra":"informacion","Lista1":L1,"Lista2":L2,"mislistas":milistas,"distancia":distancias}
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

def procesamiento(request,pk):
    umbral=0
    if request.method == 'POST':
        umbral=int(request.POST['umbral'])
        print("me mandaste el ",umbral)
    return  render(request, "home/home.html")
    
    
def euclidea(tessiu):
    tejidosTotal = []
    for i in tessiu:
        tejido = []
        tejido.append(i.temperature)
        tejido.append(i.color)
        tejido.append(i.inflamation)
        tejidosTotal.append(tejido)      

    mEuclidea = []
    umbral=1
    for i in range(len(tejidosTotal)):
        f = []
        for j in range(len(tejidosTotal)):
            #f.append(round(math.dist(tejidosTotal[i],tejidosTotal[j] )))   
            dis=(math.dist(tejidosTotal[i],tejidosTotal[j] ))
                
            #mEuclidea.append(f)
            if dis>umbral:
                print(i,j,"No",dis)
            else:
                print(i,j,"Si",dis)

    return (mEuclidea)
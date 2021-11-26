from django.shortcuts import render
from .models import tessiu
import math

def homee(request):
    Lista=tessiu.objects.get_queryset()
    L1,L2=procesaLista(Lista)
    umbral=0
    if request.method == 'POST':
        umbral=int(request.POST['umbral'])
        print("me mandaste el ",umbral)
    distancias=distacnciaeu(Lista,umbral)
    milistas=[Lista,L1,L2]
    template_name="home/home.html"
    diccio= {'l':Lista,"otra":"informacion","Lista1":L1,"Lista2":L2,"mislistas":milistas,"distancia":distancias}
    print(distancias)
   
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


    
    
def distacnciaeu(tessiu,umbral):
    valorestej = []
    for i in tessiu:
        tejido = []
        tejido.append(i.temperature)
        tejido.append(i.color)
        tejido.append(i.inflamation)
        valorestej.append(tejido)      

    valores = []
    umbral=umbral
    for i in range(len(valorestej)):
        for j in range(len(valorestej)):
        
            dis=(math.dist(valorestej[i],valorestej[j] ))
                
            if dis>umbral:
                valores.append([i,"  ",j," Distancia :",dis,"No"])
                
            else:
                valores.append([i,"  ",j," Distancia :",dis,"Si"])
    
    return (valores)
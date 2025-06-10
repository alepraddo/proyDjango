from django.shortcuts import render
from . models import Cafeteria

def lista_cafeterias(request):
    cafeterias = Cafeteria.objects.order_by('-fecha_creacion')
    return render(request, "cafeterias/lista_cafeterias.html",
                  {"cafeterias": cafeterias})

from django.http import HttpResponse
def evaluacion2(request):
    return HttpResponse ("Esto es la evaluacion2")
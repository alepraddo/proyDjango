from django.shortcuts import render
from .models import Cafeteria

def lista_cafeterias(request):
    cafeterias = Cafeteria.objects.all()
    return render(request, 'cafeterias/lista_cafeterias.html', {'cafeterias': cafeterias})

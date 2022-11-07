from django.shortcuts import render
from miapp.models import amigos
# Create your views here.
def mostrar_amigos(request):
    
    a1 = amigos(nombre = "juan", apellido = "cruz", edad = "20",cumpleaños = "2000-01-14")
    a2 = amigos(nombre = "brian", apellido = "amezquita", edad = "22",cumpleaños = "2000-01-23")
    
    return render(request, "amigos.html", {"amigos":[a1, a2]})

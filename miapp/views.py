from django.shortcuts import render
from miapp.models import amigos
# Create your views here.
def mostrar_amigos(request):
    
    a1 = amigos(nombre = "sebastian", apellido = "amezquita", edad = "20",cumpleaños = "2000-01-14")
    a2 = amigos(nombre = "brian", apellido = "amezquita", edad = "22",cumpleaños = "2000-01-23")
    a3 = amigos(nombre = "nicolas" , apellido = "amezquita", edad = "35", cumpleaños = "1998-03-30")
    
    return render(request, "amigos.html", {"amigos":[a1, a2, a3]})

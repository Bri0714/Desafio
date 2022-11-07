from django.urls import path
from miapp.views import mostrar_amigos

urlpatterns = [
    path("amigos/", mostrar_amigos)
]

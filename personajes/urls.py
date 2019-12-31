from django.urls import path 
from .views import PersonajeList, PersonajeDetail, PersonajeCreate, SearchList

urlpatterns = [
    path("", PersonajeList.as_view(), name="personajes"),
    path('personaje/<name>/', PersonajeDetail.as_view(), name='personaje'),
    path('create/', PersonajeCreate.as_view(), name='create'),
    path('buscar/', SearchList.as_view(), name='search'),
]
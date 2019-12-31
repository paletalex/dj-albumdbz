from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Personaje
from .forms import PersonajeForm
from django.db.models import Q

class SearchList(ListView):
    model = Personaje
    template_name = 'personajes/search.html'

    def get_queryset(self): # new
        queryset = self.request.GET.get('buscar')
        personajes = Personaje.objects.filter(
            Q(name__icontains=queryset) | Q(description__icontains=queryset)
        ).distinct()
        return personajes

# Create your views here.
class PersonajeList(ListView):
    template_name = 'personajes/personajes.html'
    model = Personaje

class PersonajeDetail(DetailView):
    template_name = 'personajes/personaje.html'
    context_object_name = 'p'

    def get_object(self):
        return get_object_or_404(Personaje, name=self.kwargs['name'])

class PersonajeCreate(CreateView):
    template_name = 'personajes/create_personaje.html'
    form_class = PersonajeForm
    success_url = reverse_lazy('personajes')
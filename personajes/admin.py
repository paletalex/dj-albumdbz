from django.contrib import admin
from .models import Personaje
# Register your models here.

class PersonajeAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'raza', 'universe']

admin.site.register(Personaje, PersonajeAdmin)
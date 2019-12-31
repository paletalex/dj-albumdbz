from django import forms
from .models import Personaje

class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = ['name', 'description', 'age', 'type', 'raza', 'universe', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control mb-4', 'placeholder':'Escribe el nombre de tu personaje'}),
            'description': forms.Textarea(attrs={'class':'form-control mb-4', 'placeholder':'Descripcion', 'rows':3}),
            'age': forms.TextInput(attrs={'class':'form-control mb-4', 'placeholder':'Edad'}),
            'type': forms.TextInput(attrs={'class':'form-control mb-4', 'placeholder':'Tipo'}),
            'raza': forms.TextInput(attrs={'class':'form-control mb-4', 'placeholder':'Raza'}),
            'universe': forms.TextInput(attrs={'class':'form-control mb-4', 'placeholder':'Universo'}),
            'image': forms.URLInput(attrs={'class':'form-control mb-4', 'placeholder':'Enlace o URL de la imagen'}),
            
        }
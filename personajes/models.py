from django.db import models

# Create your models here.
class Personaje(models.Model):
    name = models.CharField('Nombre', max_length=200)
    description = models.TextField('Descripcion')
    image = models.URLField('Imagen', max_length=200)
    age = models.CharField('Edad', max_length=20)
    type = models.CharField('Tipo', max_length=200)
    raza = models.CharField('Raza', max_length=200)
    universe = models.CharField('Universo', max_length=200)
    
    class Meta:
        verbose_name = 'Personaje'
        verbose_name_plural = 'Personajes'
        ordering = ['-id']
        
    def __str__(self):
        return self.name
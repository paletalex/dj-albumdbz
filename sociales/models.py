from django.db import models

# Create your models here.
class Social(models.Model):
    key = models.SlugField('Clave')
    name = models.CharField('Nombre', max_length=50)
    link = models.URLField('Enlace', max_length=200)

    class Meta:
        verbose_name = 'Red social'
        verbose_name_plural = 'Redes sociales'

    def __str__(self):
        return self.name
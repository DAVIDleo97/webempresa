from distutils.command.upload import upload
from django.db import models

# Create your models here.
#modelos siempre en singular
class Page(models.Model):
    title= models.CharField(max_length= 200, verbose_name="Título")
    content= models.TextField(verbose_name= "Contenido")
    created= models.DateTimeField(auto_now_add= True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now= True, verbose_name="Fecha de actualización")
    class Meta:
        verbose_name="pagina"
        verbose_name_plural="paginas"
        ordering=['created']

    def __str__(self):
        return self.title
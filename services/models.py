from distutils.command.upload import upload
from django.db import models

# Create your models here.
#modelos siempre en singular
class Service(models.Model):
    title= models.CharField(max_length= 200, verbose_name="Título")
    subtitle= models.CharField(max_length= 200, verbose_name="Subtítulo")
    image= models.ImageField(verbose_name= "Imagen", upload_to="services")
    content= models.TextField(verbose_name= "Contenido")
    created= models.DateTimeField(auto_now_add= True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now= True, verbose_name="Fecha de actualización")
    class Meta:
        verbose_name="servicio"
        verbose_name_plural="servicios"
        ordering=['created']

    def __str__(self):
        return self.title




from django.db import models
from django.utils.timezone import now
#importar modelo User
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200, verbose_name="Nombre")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="categoría"
        verbose_name_plural="categoías"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=200, verbose_name="Título")
    image=models.ImageField(verbose_name="Imagen", upload_to="blog")
    content=models.TextField(verbose_name="Contenido")
    published=models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    author=models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category, verbose_name="Categorías", related_name="getBlogs")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="entrada"
        verbose_name_plural="entradas"
        ordering=['-created']

    def __str__(self):
        return self.title
from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

# Create your views here.

def blog(request):
    blogs=Blog.objects.all()
    return render(request, "blog/blog.html", {'blogs': blogs})
    
# entradas por cada categoria    
def category(request, categoryId):
    category= get_object_or_404(Category, id=categoryId)

    #filtrar las entradas de esa categoria
    #blogs=Blog.objects.filter(categories=category)
    #return render(request, "blog/category.html", {'category': category, 'blogs':blogs}) 
    return render(request, "blog/category.html", {'category': category}) 

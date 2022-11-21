from django.shortcuts import render

# Create your views here.

def ctx_dict(request):
    ctx={'test':"hola mundo"}
    return ctx
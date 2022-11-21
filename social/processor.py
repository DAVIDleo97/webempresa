from .models import Social

def ctx_dict(request):
    ctx={}
    socialList=Social.objects.all()
    #agregar datos en el diccionario
    for social in socialList:
        ctx[social.key]=social.url
    return ctx
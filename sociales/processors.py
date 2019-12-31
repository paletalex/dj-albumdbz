from .models import Social

def ctx_sociales(request):
    ctx = {}
    redes = Social.objects.all()
    for r in redes:
        ctx[r.key] = r.link
    return ctx
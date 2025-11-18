from django.shortcuts import render
from .models import Animal, Refugio, Centro, Vacuna, Animal_vacunas, Revision_veterinaria
from django.db.models import Avg, Max, Min, Q, Prefetch
from django.views.defaults import page_not_found


# Create your views here.


def index(request):
    return render(request, 'index.html') 

def Ejercicio1(request, animal_contiene, refugio_contiene):
    queryset_ej1 = Animal.objects.select_related('centro').filter(nombre__contains=animal_contiene, centro__refugio__nombre__contains=refugio_contiene)
    return render(request, 'appexamen/ejercicio1.html', {"ejercicio1_resultados":queryset_ej1})



#   PÁGINAS DE ERRORES
def mi_error_404(request, exception=None):
    return render(request, 'Errores/404.html',None,None,404)

def mi_error_400(request, exception=None):
    return render(request, 'Errores/400.html',None,None,400)

def mi_error_403(request, exception=None):
    return render(request, 'Errores/403.html',None,None,403)

def mi_error_500(request, exception=None):
    return render(request, 'Errores/500.html',None,None,500)
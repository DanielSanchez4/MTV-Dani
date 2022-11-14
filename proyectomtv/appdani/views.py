
from appdani.models import familia

from django.http import HttpResponse

# Create your views here.


def listado_familia(request):
    listado = familia.objects.all()

    cadena_respuesta = ""
    for FAMILIA in listado:
     
        cadena_respuesta += f"({FAMILIA.nombre},{FAMILIA.edad},{FAMILIA.fecha}" + " | "

    return HttpResponse(cadena_respuesta)
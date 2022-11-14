from django.http import HttpResponse
from datetime import datetime
from django.template import Template ,  Context



def vista_saludo(request):
    return HttpResponse ("<h1>Hola mundo </h1>")


def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"hoy es {hoy} - Bienvenid@ {nombre}"

    return HttpResponse(respuesta)


def anio_nacimiento(request, edad):
    
    edad = int(edad)

    nacimiento = datetime.now().year - edad

    return HttpResponse(f"Naciste en {nacimiento}")


def informacion_familia(request):
    archivo = open(r"C:\Users\Usuario\OneDrive\Escritorio\MTV-Dani\proyectomtv\proyectomtv\templates\plantilla_familia.html")    

    plantilla = Template(archivo.read())

    archivo.close()

    nombres = ["nombre: Daiana Valenzuela" ,

    "nombre: Jimena Godoy" ,
    "nombre: Martin Sanchez"

    ]

    edades = ["Edad: 25",
    "Edad: 44",
    "Edad: 49"
    ]

    datos = {"Nombres": nombres , "Edades": edades}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)
    

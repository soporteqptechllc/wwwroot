from django.shortcuts import render
from django.http import HttpResponse
from .models import producciondiaria

def informacion(request):
    return render(request, "of/vista.html")

def vista(request):
    return HttpResponse("visualizar los datos de produccion")

def validar(request):
    return HttpResponse("Validar los datos para generar la orden de produccion")

#def editar(request):
#    return render(request, "editar.html")

def editar(request):
    greeting = {}
    tabla = producciondiaria.objects.all().order_by('id')
    greeting['tabla'] = tabla
    greeting['heading'] = "Producción Diaría En Cremas"
    greeting['pageview'] = "Consumo de Cremas Por Turno"
    return render (request,'components-editabletables.html',greeting) 
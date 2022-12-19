from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.


def empleado(request):

    empleado= Empleado(nombre= "Pedro", apellido= "Lucero", legajo=2054)
    empleado.save()
    cadena=f"empleado guardado: Nombre: {empleado.nombre}, apellido: {empleado.apellido}, legajo: {empleado.legajo}"
    return render(request, "AppSuper/empleados.html")


def gerente(request):

    gerente= Gerente(nombre= "jose", apellido= "salgado", legajo=7021)
    gerente.save()
    return render(request, "AppSuper/gerentes.html")



    
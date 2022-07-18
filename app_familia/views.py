from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Familia


# Create your views here.

def inicio(request):

    plantilla= loader.get_template("inicio.html")

    documento = plantilla.render()

    return HttpResponse(documento)

def yo(request):

    plantilla= loader.get_template("yo.html")

    documento = plantilla.render()

    return HttpResponse(documento)


def padre(request):
    
    plantilla= loader.get_template("padre.html")

    documento = plantilla.render()

    return HttpResponse(documento)


def madre(request):
    
    plantilla= loader.get_template("madre.html")

    documento = plantilla.render()

    return HttpResponse(documento)


def hermano(request):
    
    plantilla= loader.get_template("hermano.html")

    documento = plantilla.render()

    return HttpResponse(documento)

def ver_yo(self):

    lista= Familia.objects.filter(parentesco= "Yo")

    return render(self, "yo.html", {"lista": lista})

def ver_padre(self):

    lista= Familia.objects.filter(parentesco= "Padre")

    return render(self, "padre.html", {"lista": lista})

def ver_hermano(self):

    lista= Familia.objects.filter(parentesco= "Hermano")

    return render(self, "hermano.html", {"lista": lista})

def ver_madre(self):

    lista= Familia.objects.filter(parentesco= "Madre")

    return render(self, "madre.html", {"lista": lista})
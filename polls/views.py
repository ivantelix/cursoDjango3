from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Persona


# Create your views here.

def index(request):
    context = {'context': 'Prueba de contexto'}
    return render(request, 'polls/index.html')

def create(request):
    if request.method == 'POST':
        persona = Persona()

        persona.nombre = request.POST['nombre']
        persona.apellido = request.POST['apellido']
        persona.dni = request.POST['dni']

        persona.save()

        return HttpResponseRedirect('/polls')
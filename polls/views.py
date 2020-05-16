from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Persona
from .forms import PersonaForm


# Create your views here.

def index(request):
    personas = Persona.objects.all()

    return render(request, 'polls/listar.html', {'personas' : personas})

def getForm(request):
    return render(request, 'polls/index.html')

def create(request):
    if request.method == 'POST':
        persona = Persona()

        persona.nombre = request.POST['nombre']
        persona.apellido = request.POST['apellido']
        persona.dni = request.POST['dni']

        persona.save()

        return HttpResponseRedirect('/polls')

def detail(request, question_id):
    persona = Persona.objects.get(id=question_id)

    return render(request, 'polls/detalles.html', {'persona' : persona})


###############################################################

###############################################################
def getFormModelForm(request):
    form = PersonaForm()

    return render(request, 'polls/createFormModelForm.html', {'formPersona':form})


def createWithModelForm(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/polls')


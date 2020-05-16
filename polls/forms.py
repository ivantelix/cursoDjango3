from django.forms import ModelForm
from .models import Persona

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'dni']
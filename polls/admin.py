from django.contrib import admin

# Register your models here.
from .models import Persona, Familia

class FamiliaAdminInline(admin.StackedInline):
    model = Familia
    fields = ['nombre', 'parentesco']

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'dni']

    inlines = [FamiliaAdminInline]

admin.site.register(Persona, PersonaAdmin)
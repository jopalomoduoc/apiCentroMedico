from django.contrib import admin
from .models import Paciente, Region, Comuna, Sucursal, Especialidad, Pago, Persona, Medico, Agenda

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Sucursal)
admin.site.register(Especialidad)
admin.site.register(Pago)
admin.site.register(Persona)
admin.site.register(Medico)
admin.site.register(Agenda)

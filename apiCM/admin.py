from django.contrib import admin
from .models import Paciente, Region, Comuna, Sucursal, Especialidad, Pago, Agenda, Trabajador, Cargo

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Sucursal)
admin.site.register(Especialidad)
admin.site.register(Pago)
admin.site.register(Trabajador)
admin.site.register(Cargo)
admin.site.register(Agenda)

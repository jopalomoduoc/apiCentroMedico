from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Paciente, Region, Comuna, Sucursal, Especialidad, Pago, Persona, Medico, Agenda

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['correo', 'id_persona', 'password', 'repeatPassword', 'celular', 'enfermedades', 'alergias', 'sexo']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'nombre']

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id', 'nombre', 'id_region']

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ['id', 'nombre', 'id_comuna']

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ['id', 'nombre']

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['id', 'tipo', 'id_agenda', 'fecha_pago', 'monto_pago']

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'rut', 'nombre', 'apellido', 'direccion', 'id_comuna']

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'correo', 'id_persona', 'id_especialidad']

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['id', 'correo', 'id_medico', 'fecha_inicio', 'fecha_termino', 'id_sucursal']
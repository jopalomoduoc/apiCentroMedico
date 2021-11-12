from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cargo, Paciente, Region, Comuna, Sucursal, Especialidad, Pago, Agenda, Trabajador

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'nombre']

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id', 'nombre', 'region']

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ['id', 'nombre', 'comuna']

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['correo', 'rut', 'nombre', 'apellido', 'direccion', 'comuna', 'password', 'repeatPassword', 'celular', 'enfermedades', 'alergias', 'sexo']

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ['id', 'especialidad']

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['id', 'cargo']

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ['correo', 'cargo', 'rut', 'nombre', 'apellido', 'direccion', 'comuna']

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['id', 'paciente', 'medico', 'especialidad', 'fecha', 'hora', 'sucursal']

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['id', 'tipo', 'agenda', 'fecha', 'monto']
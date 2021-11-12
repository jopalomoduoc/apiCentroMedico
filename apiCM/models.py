from django.db import models

# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=90, verbose_name='Nombre de Region')
    def __str__(self):
      return self.nombre

class Comuna(models.Model):
    nombre =  models.CharField(max_length=90, verbose_name='Nombre de Comuna') 
    region =  models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre Sucursal')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE) 
    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    correo = models.CharField(primary_key=True, max_length=50, verbose_name='Correo de Usuario')
    rut = models.CharField(max_length=14, verbose_name='Rut Persona')
    nombre = models.CharField(max_length=50, verbose_name='Nombre Persona')
    apellido = models.CharField(max_length=50, verbose_name='Apellido Persona')
    direccion = models.CharField(max_length=50, verbose_name='Dirección Persona')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    password = models.CharField(max_length=12, verbose_name='Contraseña')
    repeatPassword = models.CharField(max_length=12, verbose_name='Repetir Contraseña')
    celular = models.IntegerField(verbose_name="Celular")
    enfermedades = models.TextField(max_length=255, verbose_name='Enfermedades')
    alergias = models.TextField(max_length=255, verbose_name='Alergias')
    sexo = models.CharField(max_length=15, verbose_name='Sexo')

    def __str__(self):
        return self.correo

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=50, verbose_name='Nombre Especialidad')

    def __str__(self):
        return self.especialidad

class Cargo(models.Model):
    cargo = models.CharField(max_length=50, verbose_name='Cargo')

    def __str__(self):
        return self.cargo

class Trabajador(models.Model):
    correo = models.CharField(primary_key=True, max_length=50, verbose_name='Correo de Trabajador')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    rut = models.CharField(max_length=14, verbose_name='Rut Trabajador')
    nombre = models.CharField(max_length=50, verbose_name='Nombre Trabajador')
    apellido = models.CharField(max_length=50, verbose_name='Apellido Trabajador')
    direccion = models.CharField(max_length=50, verbose_name='Dirección Trabajador')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return self.correo

class Agenda(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico =  models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE) 
    fecha = models.DateField(verbose_name='Fecha de Cita')
    hora = models.TimeField(verbose_name='Hora de Cita')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __int__(self):
        return self.id

class Pago(models.Model):
    tipo = models.CharField(max_length=50, verbose_name='Tipo de Pago')
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name='Fecha de Pago')
    monto = models.IntegerField(verbose_name='Monto de Pago')

    def __int__(self):
        return self.id
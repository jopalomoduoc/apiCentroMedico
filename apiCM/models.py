from django.db import models

# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=90, verbose_name='Nombre de Region')
    def __str__(self):
      return self.nombre

class Comuna(models.Model):
    nombre =  models.CharField(max_length=90, verbose_name='Nombre de Comuna') 
    id_region =  models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    rut = models.CharField(max_length=14, verbose_name='Rut Persona')
    nombre = models.CharField(max_length=50, verbose_name='Nombre Persona')
    apellido = models.CharField(max_length=50, verbose_name='Apellido Persona')
    direccion = models.CharField(max_length=50, verbose_name='Dirección Persona')
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    correo = models.CharField(primary_key=True, max_length=50, verbose_name='Correo de Usuario')
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    password = models.CharField(max_length=12, verbose_name='Contraseña')
    repeatPassword = models.CharField(max_length=12, verbose_name='Repetir Contraseña')
    celular = models.IntegerField(verbose_name="Celular")
    enfermedades = models.TextField(max_length=255, verbose_name='Enfermedades')
    alergias = models.TextField(max_length=255, verbose_name='Alergias')
    sexo = models.CharField(max_length=15, verbose_name='Sexo')

    def __str__(self):
        return self.correo

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre Sucursal')
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE) 
    def __str__(self):
        return self.nombre
    
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre Especialidad')

    def __str__(self):
        return self.nombre 

class Medico(models.Model):
      id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE) 
      id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
def __str__(self):
    return self.id_persona         

class Agenda(models.Model):
    correo = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_medico =  models.ForeignKey(Medico, on_delete=models.CASCADE)  
    fecha_inicio = models.DateField(verbose_name='Fecha de Inicio')
    fecha_termino = models.DateField(verbose_name='Fecha de Termino')
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return self.correo

class Pago(models.Model):
    tipo = models.CharField(max_length=50, verbose_name='Tipo de Pago')
    id_agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    fecha_pago = models.DateField(verbose_name='Fecha de Pago')
    monto_pago = models.IntegerField(verbose_name='Monto de Pago')   
def __str__(self):
    return self.tipo
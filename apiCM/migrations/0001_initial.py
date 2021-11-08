# Generated by Django 3.2.9 on 2021-11-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('correo', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Correo de Usuario')),
                ('nombre', models.CharField(max_length=25, verbose_name='Nombre de Usuario')),
                ('apellido', models.CharField(max_length=25, verbose_name='Apellido de Usuario')),
                ('password', models.CharField(max_length=12, verbose_name='Contraseña')),
                ('repeatPassword', models.CharField(max_length=12, verbose_name='Repetir Contraseña')),
                ('direccion', models.TextField(max_length=255, verbose_name='Dirección')),
                ('celular', models.IntegerField(verbose_name='Celular')),
                ('enfermedades', models.TextField(max_length=255, verbose_name='Enfermedades')),
                ('alergias', models.TextField(max_length=255, verbose_name='Alergias')),
                ('sexo', models.CharField(max_length=15, verbose_name='Sexo')),
            ],
        ),
    ]
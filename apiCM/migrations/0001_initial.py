# Generated by Django 3.2.9 on 2021-11-12 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de Cita')),
                ('hora', models.TimeField(verbose_name='Hora de Cita')),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=50, verbose_name='Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90, verbose_name='Nombre de Comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=50, verbose_name='Nombre Especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90, verbose_name='Nombre de Region')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('correo', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Correo de Trabajador')),
                ('rut', models.CharField(max_length=14, verbose_name='Rut Trabajador')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Trabajador')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido Trabajador')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direcci??n Trabajador')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiCM.cargo')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiCM.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Sucursal')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiCM.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo de Pago')),
                ('fecha', models.DateField(verbose_name='Fecha de Pago')),
                ('monto', models.IntegerField(verbose_name='Monto de Pago')),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiCM.agenda')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('correo', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Correo de Usuario')),
                ('rut', models.CharField(max_length=14, verbose_name='Rut Persona')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Persona')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido Persona')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direcci??n Persona')),
                ('password', models.CharField(max_length=12, verbose_name='Contrase??a')),
                ('repeatPassword', models.CharField(max_length=12, verbose_name='Repetir Contrase??a')),
                ('celular', models.IntegerField(verbose_name='Celular')),
                ('enfermedades', models.TextField(max_length=255, verbose_name='Enfermedades')),
                ('alergias', models.TextField(max_length=255, verbose_name='Alergias')),
                ('sexo', models.CharField(max_length=15, verbose_name='Sexo')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiCM.comuna')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiCM.region'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='especialidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiCM.especialidad'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiCM.trabajador'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiCM.paciente'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiCM.sucursal'),
        ),
    ]

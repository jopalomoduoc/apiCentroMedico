# Generated by Django 3.2.9 on 2021-11-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiCM', '0003_auto_20211111_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='correo',
            field=models.CharField(default=1, max_length=50, verbose_name='Correo del Medico'),
            preserve_default=False,
        ),
    ]
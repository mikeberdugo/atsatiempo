# Generated by Django 5.0.6 on 2024-07-22 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0006_alter_can102experiencia_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='can102experiencia',
            name='fecha_final',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='can102experiencia',
            name='fecha_inicial',
            field=models.DateField(blank=True, null=True),
        ),
    ]

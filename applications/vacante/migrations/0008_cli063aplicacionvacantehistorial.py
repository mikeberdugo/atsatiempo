# Generated by Django 5.0.6 on 2024-10-28 18:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacante', '0007_alter_cli056aplicacionvacante_estado_aplicacion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cli063AplicacionVacanteHistorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.IntegerField(choices=[(1, 'Aplicado'), (2, 'Entrevista Programada'), (3, 'Entrevista Aprobada'), (4, 'Entrevista No Aprobada'), (5, 'Prueba Programada'), (6, 'Prueba Superada'), (7, 'Prueba No Superada'), (8, 'Seleccionado'), (9, 'Finalizada'), (10, 'Cancelada'), (11, 'Desiste')])),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('aplicacion_vacante_056', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historial', to='vacante.cli056aplicacionvacante')),
                ('usuario_id_genero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Historial de Aplicación a Vacante',
                'verbose_name_plural': 'Historiales de Aplicaciones a Vacantes',
                'db_table': 'cli_056_aplicacion_vacante_historial',
            },
        ),
    ]
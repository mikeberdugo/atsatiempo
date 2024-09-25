# Generated by Django 5.0.6 on 2024-09-25 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidato', '0001_initial'),
        ('cliente', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cli052VacanteHardSkillsId054',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'cli_052_vacante_hard_skills_id_054',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cli052VacanteSoftSkillsId053',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'cli_052_vacante_soft_skills_id_053',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cli053SoftSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estado_id_001', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.cat001estado')),
            ],
            options={
                'verbose_name': 'SOFT_SKILL',
                'db_table': 'cli_053_soft_skill',
            },
        ),
        migrations.CreateModel(
            name='Cli054HardSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estado_id_001', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.cat001estado')),
            ],
            options={
                'verbose_name': 'HARD_SKILL',
                'db_table': 'cli_054_hard_skill',
            },
        ),
        migrations.CreateModel(
            name='Cli055ProfesionEstudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('estado_id_001', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.cat001estado')),
            ],
            options={
                'verbose_name': 'PROFESION_ESTUDIO',
                'verbose_name_plural': 'PROFESIONES_ESTUDIOS',
                'db_table': 'cli_055_profesion_estudio',
            },
        ),
        migrations.CreateModel(
            name='Cli052Vacante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('numero_posiciones', models.IntegerField()),
                ('experiencia_requerida', models.IntegerField(choices=[(1, '0 a 6 Meses'), (2, '1 año a 2 años'), (3, 'Más de 2 años'), (4, 'Sin Experiencia')])),
                ('funciones_responsabilidades', models.TextField()),
                ('salario', models.IntegerField(blank=True, null=True)),
                ('estado_vacante', models.IntegerField(choices=[(1, 'Abierta'), (2, 'Cerrada'), (3, 'Cancelada')], default=1)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.cat004ciudad')),
                ('cliente_id_051', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cli051cliente')),
                ('estado_id_001', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='common.cat001estado')),
                ('soft_skills_id_053', models.ManyToManyField(to='vacante.cli053softskill')),
                ('hard_skills_id_054', models.ManyToManyField(to='vacante.cli054hardskill')),
                ('profesion_estudio_id_055', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacante.cli055profesionestudio')),
            ],
            options={
                'verbose_name': 'VACANTE',
                'verbose_name_plural': 'VACANTES',
                'db_table': 'cli_052_vacante',
            },
        ),
        migrations.CreateModel(
            name='Cli056AplicacionVacante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aplicacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado_aplicacion', models.IntegerField(choices=[(1, 'En proceso'), (2, 'Exitoso'), (3, 'Cancelado'), (4, 'Terminado'), (5, 'Desiste')], default=1)),
                ('candidato_101', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aplicaciones', to='candidato.can101candidato')),
                ('vacante_id_052', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aplicaciones', to='vacante.cli052vacante')),
            ],
            options={
                'verbose_name': 'APLICACIÓN A VACANTE',
                'verbose_name_plural': 'APLICACIONES A VACANTES',
                'db_table': 'cli_056_aplicacion_vacante',
                'unique_together': {('candidato_101', 'vacante_id_052')},
            },
        ),
    ]

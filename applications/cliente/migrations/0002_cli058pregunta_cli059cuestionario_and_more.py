# Generated by Django 5.0.6 on 2024-10-02 19:53

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0001_initial'),
        ('cliente', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cli058Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.TextField(blank=True)),
                ('respuesta', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('pregunta_correlacion', models.TextField(blank=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cli051cliente')),
                ('estado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='common.cat001estado')),
            ],
            options={
                'verbose_name': 'PREGUNTA',
                'verbose_name_plural': 'PREGUNTAS',
                'db_table': 'cli_058_pregunta',
            },
        ),
        migrations.CreateModel(
            name='Cli059Cuestionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_cuestionario', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('estado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='common.cat001estado')),
            ],
            options={
                'verbose_name': 'CUESTIONARIO',
                'verbose_name_plural': 'CUESTIONARIOS',
                'db_table': 'cli_059_cuestionario',
            },
        ),
        migrations.CreateModel(
            name='Cli061AsignacionCandidatoCuestionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('p', 'Pendiente'), ('r', 'Realizado')], default='p', max_length=1)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidato.can101candidato')),
                ('cuestionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cli059cuestionario')),
                ('estado_relacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.cat001estado')),
            ],
            options={
                'verbose_name': 'CUESTIONARIO',
                'verbose_name_plural': 'CUESTIONARIOS',
                'db_table': 'cli_061_asignacion_candidato_cuestionario',
            },
        ),
        migrations.CreateModel(
            name='Cli062Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('fecha_hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('asignacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cli061asignacioncandidatocuestionario')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidato.can101candidato')),
                ('estado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='common.cat001estado')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cli058pregunta')),
            ],
            options={
                'verbose_name': 'RESPUESTA',
                'verbose_name_plural': 'RESPUESTAS',
                'db_table': 'cli_062_respuesta',
            },
        ),
        migrations.CreateModel(
            name='Cli060CuestionarioPregunta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_asignacion', models.DateField(auto_now_add=True)),
                ('cli058pregunta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.cli058pregunta')),
                ('cli059cuestionario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.cli059cuestionario')),
            ],
            options={
                'verbose_name': 'CUESTIONARIO_PREGUNTA',
                'verbose_name_plural': 'CUESTIONARIOS_PREGUNTAS',
                'db_table': 'cli_060_cuestionario_pregunta',
                'unique_together': {('cli059cuestionario', 'cli058pregunta')},
            },
        ),
    ]

# Generated by Django 5.0.6 on 2024-10-28 18:48


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Psi201Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.CharField(blank=True, max_length=255, null=True)),
                ('es_invertida', models.BooleanField(blank=True, null=True)),
                ('factor', models.CharField(blank=True, max_length=1, null=True)),
                ('subfactor', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'psi_201_pregunta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Psi202Respuesta',
            fields=[
                ('id_respuesta', models.IntegerField(primary_key=True, serialize=False)),
                ('respuesta', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'psi_202_respuesta',
                'managed': False,
            },
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-18 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0003_can101candidato_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='can101candidato',
            name='skills',
            field=models.ManyToManyField(related_name='candidatos_skill', to='candidato.can104skill'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-09-06 15:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacante', '0003_alter_cli052vacante_experiencia_requerida'),
    ]

    operations = [
        migrations.AddField(
            model_name='cli052vacante',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

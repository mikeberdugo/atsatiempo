# Generated by Django 5.0.6 on 2024-09-09 18:13

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokenautorizacion',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 10, 18, 13, 20, 364134, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='usuariobase',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.grupo'),
        ),
    ]

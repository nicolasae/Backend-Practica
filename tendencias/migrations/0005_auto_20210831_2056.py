# Generated by Django 3.2.6 on 2021-08-31 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendencias', '0004_programasnoofrecidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programasnoofrecidos',
            name='DuracionACAños',
            field=models.FloatField(null=True, verbose_name='Duración (AC) Años'),
        ),
        migrations.AlterField(
            model_name='programasnoofrecidos',
            name='DuracionRCAños',
            field=models.FloatField(null=True, verbose_name='Duración (RC) Años'),
        ),
    ]

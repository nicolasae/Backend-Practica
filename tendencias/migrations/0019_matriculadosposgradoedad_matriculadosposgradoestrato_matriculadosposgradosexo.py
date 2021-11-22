# Generated by Django 3.2.6 on 2021-09-28 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendencias', '0018_rename_semeste_matriculadospregradoedad_semestre'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatriculadosPosgradoEdad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Programa', models.CharField(max_length=255, null=True, verbose_name='Programa Académico')),
                ('Semestre', models.CharField(max_length=255, null=True, verbose_name='Semestre')),
                ('MenorA17', models.IntegerField(null=True, verbose_name='MenorA17')),
                ('MayorA17MenorA22', models.IntegerField(null=True, verbose_name='MayorA17MenorA22')),
                ('Edad22', models.IntegerField(null=True, verbose_name='Edad22')),
                ('Edad23', models.IntegerField(null=True, verbose_name='Edad23')),
                ('Edad24', models.IntegerField(null=True, verbose_name='Edad24')),
                ('Edad25', models.IntegerField(null=True, verbose_name='Edad25')),
                ('MayorA26MenorA31', models.IntegerField(null=True, verbose_name='MayorA26MenorA31')),
                ('MayorA31', models.IntegerField(null=True, verbose_name='MayorA31')),
                ('Total', models.IntegerField(null=True, verbose_name='Total')),
            ],
        ),
        migrations.CreateModel(
            name='MatriculadosPosgradoEstrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Programa', models.CharField(max_length=255, null=True, verbose_name='Programa Académico')),
                ('Semestre', models.CharField(max_length=255, null=True, verbose_name='Semestre')),
                ('Estrato0', models.IntegerField(null=True, verbose_name='Estrato0')),
                ('EstratoI', models.IntegerField(null=True, verbose_name='EstratoI')),
                ('EstratoII', models.IntegerField(null=True, verbose_name='EstratoII')),
                ('EstratoIII', models.IntegerField(null=True, verbose_name='EstratoIII')),
                ('EstratoIV', models.IntegerField(null=True, verbose_name='EstratoIV')),
                ('EstratoV', models.IntegerField(null=True, verbose_name='EstratoV')),
                ('EstratoVI', models.IntegerField(null=True, verbose_name='EstratoVI')),
                ('Total', models.IntegerField(null=True, verbose_name='Total')),
            ],
        ),
        migrations.CreateModel(
            name='MatriculadosPosgradoSexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Programa', models.CharField(max_length=255, null=True, verbose_name='Programa Académico')),
                ('Semestre', models.CharField(max_length=255, null=True, verbose_name='Semestre')),
                ('Masculino', models.IntegerField(null=True, verbose_name='Masculino')),
                ('Femenino', models.IntegerField(null=True, verbose_name='Femenino')),
                ('Total', models.IntegerField(null=True, verbose_name='Total')),
            ],
        ),
    ]
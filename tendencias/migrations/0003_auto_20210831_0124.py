# Generated by Django 3.2.6 on 2021-08-31 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendencias', '0002_auto_20210831_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tendencia',
            name='Graduado',
            field=models.IntegerField(null=True, verbose_name='Graduado'),
        ),
        migrations.AlterField(
            model_name='tendencia',
            name='Inscrito',
            field=models.IntegerField(null=True, verbose_name='Inscrito'),
        ),
        migrations.AlterField(
            model_name='tendencia',
            name='Matriculado',
            field=models.IntegerField(null=True, verbose_name='Matriculado'),
        ),
        migrations.AlterField(
            model_name='tendencia',
            name='PrimerCurso',
            field=models.IntegerField(null=True, verbose_name='Primer Curso'),
        ),
        migrations.AlterField(
            model_name='tendencia',
            name='Programa',
            field=models.CharField(max_length=255, null=True, verbose_name='Programa Academico'),
        ),
        migrations.AlterField(
            model_name='tendencia',
            name='Semestre',
            field=models.CharField(max_length=255, null=True, verbose_name='Semestre'),
        ),
    ]

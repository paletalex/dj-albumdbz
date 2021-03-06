# Generated by Django 3.0.1 on 2019-12-30 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('age', models.CharField(max_length=20, verbose_name='Edad')),
                ('type', models.CharField(max_length=200, verbose_name='Tipo')),
                ('raza', models.CharField(max_length=200, verbose_name='Raza')),
                ('universe', models.CharField(max_length=200, verbose_name='Universo')),
            ],
            options={
                'verbose_name': 'Personaje',
                'verbose_name_plural': 'Personajes',
                'ordering': ['-id'],
            },
        ),
    ]

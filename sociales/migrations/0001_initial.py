# Generated by Django 3.0.1 on 2019-12-30 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(verbose_name='Clave')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('link', models.URLField(verbose_name='Enlace')),
            ],
            options={
                'verbose_name': 'Red social',
                'verbose_name_plural': 'Redes sociales',
            },
        ),
    ]

# Generated by Django 5.1.1 on 2024-11-07 21:17

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Nombre')),
                ('content', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='rsc/sites', verbose_name='Imagen')),
                ('state', models.CharField(max_length=100, verbose_name='Estado')),
                ('established', models.DateField(blank=True, null=True, verbose_name='Fecha Establecido')),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
            },
        ),
        migrations.CreateModel(
            name='NationalPark',
            fields=[
                ('site_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecolibrary.site')),
            ],
            options={
                'verbose_name': 'NationalPark',
                'verbose_name_plural': 'NationalParks',
            },
            bases=('ecolibrary.site',),
        ),
        migrations.CreateModel(
            name='NaturalMonument',
            fields=[
                ('site_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecolibrary.site')),
            ],
            options={
                'verbose_name': 'NaturalMonument',
                'verbose_name_plural': 'NaturalMonuments',
            },
            bases=('ecolibrary.site',),
        ),
    ]

# Generated by Django 5.1.1 on 2024-11-07 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecolibrary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='state',
            field=models.IntegerField(choices=[(0, 'Amazonas'), (1, 'Anzoátegui'), (2, 'Apure'), (3, 'Aragua'), (4, 'Barinas'), (5, 'Bolívar'), (6, 'Carabobo'), (7, 'Cojedes'), (8, 'Delta Amacuro'), (9, 'Distrito Capital'), (10, 'Falcón'), (11, 'Guárico'), (12, 'Lara'), (13, 'Mérida'), (14, 'Miranda'), (15, 'Monagas'), (16, 'Nueva Esparta'), (17, 'Portuguesa'), (18, 'Sucre'), (19, 'Táchira'), (20, 'Trujillo'), (21, 'Vargas'), (22, 'Yaracuy'), (23, 'Zulia')], verbose_name='Estado'),
        ),
    ]

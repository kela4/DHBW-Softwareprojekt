# Generated by Django 3.0 on 2019-12-23 12:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geomodels', '0009_auto_20191223_1334'),
        ('category_living', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingareaentry',
            name='id_subcategory',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie'),
        ),
        migrations.AlterField(
            model_name='groundvalueentry',
            name='id_subcategory',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie'),
        ),
        migrations.CreateModel(
            name='SchoolEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Titel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('id_subcategory', models.ForeignKey(default=10, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie')),
            ],
            options={
                'verbose_name': 'Schule',
                'verbose_name_plural': 'Schulen',
            },
        ),
        migrations.CreateModel(
            name='PlaygroundEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Titel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('id_subcategory', models.ForeignKey(default=9, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie')),
            ],
            options={
                'verbose_name': 'Spielplatz',
                'verbose_name_plural': 'Spielplätze',
            },
        ),
    ]
# Generated by Django 3.0 on 2019-12-23 12:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geomodels', '0009_auto_20191223_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrailEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Titel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('id_subcategory', models.ForeignKey(default=12, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie')),
            ],
            options={
                'verbose_name': 'Wanderweg',
                'verbose_name_plural': 'Wanderwege',
            },
        ),
        migrations.CreateModel(
            name='MonumentEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Titel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('id_subcategory', models.ForeignKey(default=11, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie')),
            ],
            options={
                'verbose_name': 'Denkmal',
                'verbose_name_plural': 'Denkmäler',
            },
        ),
        migrations.CreateModel(
            name='ChurchEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Titel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('id_subcategory', models.ForeignKey(default=13, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie')),
            ],
            options={
                'verbose_name': 'Kirche',
                'verbose_name_plural': 'Kirchen',
            },
        ),
        migrations.CreateModel(
            name='AccommodationEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Titel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('id_subcategory', models.ForeignKey(default=14, on_delete=django.db.models.deletion.PROTECT, to='geomodels.Subcategory', verbose_name='Unterkategorie')),
            ],
            options={
                'verbose_name': 'Unterkunft',
                'verbose_name_plural': 'Unterkünfte',
            },
        ),
    ]

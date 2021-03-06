# Generated by Django 3.0 on 2020-01-13 19:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geomodels', '0010_auto_20200112_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(verbose_name='Montag'), blank=True, null=True, size=None)),
                ('tuesday', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(verbose_name='Dienstag'), blank=True, null=True, size=None)),
                ('wednesday', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(verbose_name='Mittwoch'), blank=True, null=True, size=None)),
                ('thursday', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(verbose_name='Donnerstag'), blank=True, null=True, size=None)),
                ('friday', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(verbose_name='Freitag'), blank=True, null=True, size=None)),
                ('saturday', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(verbose_name='Samstag'), blank=True, null=True, size=None)),
                ('sunday', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(verbose_name='Sonntag'), blank=True, null=True, size=None)),
            ],
            options={
                'verbose_name': 'Öffnungszeit',
                'verbose_name_plural': 'Öffnungszeiten',
            },
        ),
    ]

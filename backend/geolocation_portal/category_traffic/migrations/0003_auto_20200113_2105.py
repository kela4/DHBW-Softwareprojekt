# Generated by Django 3.0 on 2020-01-13 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category_traffic', '0002_openinghoursparkingentry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openinghoursparkingentry',
            options={'verbose_name': 'Öffnungszeit', 'verbose_name_plural': 'Öffnungszeiten'},
        ),
    ]

# Generated by Django 3.0 on 2020-01-13 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category_tourism', '0002_openinghourschurchentry_openinghoursmonumententry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openinghourschurchentry',
            options={'verbose_name': 'Öffnungszeit', 'verbose_name_plural': 'Öffnungszeiten'},
        ),
        migrations.AlterModelOptions(
            name='openinghoursmonumententry',
            options={'verbose_name': 'Öffnungszeit', 'verbose_name_plural': 'Öffnungszeiten'},
        ),
    ]

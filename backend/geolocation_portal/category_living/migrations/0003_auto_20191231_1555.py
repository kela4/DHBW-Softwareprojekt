# Generated by Django 3.0 on 2019-12-31 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_living', '0002_auto_20191223_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groundvalueentry',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preis'),
        ),
    ]
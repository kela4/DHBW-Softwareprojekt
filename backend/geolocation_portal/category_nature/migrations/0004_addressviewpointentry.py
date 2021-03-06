# Generated by Django 3.0 on 2020-01-13 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geomodels', '0012_address'),
        ('category_nature', '0003_auto_20200113_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressViewpointEntry',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.Address')),
                ('viewpoint_entry', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='category_nature.ViewpointEntry')),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adressen',
            },
            bases=('geomodels.address',),
        ),
    ]

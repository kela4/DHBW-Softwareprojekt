# Generated by Django 3.0 on 2020-01-13 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geomodels', '0012_address'),
        ('category_trash', '0007_auto_20200113_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothingentry',
            name='openingHours',
        ),
        migrations.AddField(
            model_name='clothingentry',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Beschreibung'),
        ),
        migrations.AddField(
            model_name='glassentry',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Beschreibung'),
        ),
        migrations.AddField(
            model_name='recyclingcentreentry',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Beschreibung'),
        ),
        migrations.CreateModel(
            name='AddressRecyclingcentreEntry',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.Address')),
                ('recyclingcentre_entry', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='category_trash.RecyclingcentreEntry')),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adressen',
            },
            bases=('geomodels.address',),
        ),
        migrations.CreateModel(
            name='AddressIlluminantEntry',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.Address')),
                ('illuminant_entry', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='category_trash.IlluminantEntry')),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adressen',
            },
            bases=('geomodels.address',),
        ),
        migrations.CreateModel(
            name='AddressGlassEntry',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.Address')),
                ('glass_entry', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='category_trash.GlassEntry')),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adressen',
            },
            bases=('geomodels.address',),
        ),
        migrations.CreateModel(
            name='AddressElectroEntry',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.Address')),
                ('electro_entry', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='category_trash.ElectroEntry')),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adressen',
            },
            bases=('geomodels.address',),
        ),
        migrations.CreateModel(
            name='AddressClothingEntry',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.Address')),
                ('clothing_entry', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='category_trash.ClothingEntry')),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adressen',
            },
            bases=('geomodels.address',),
        ),
        migrations.CreateModel(
            name='AddressBatteryEntry',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.Address')),
                ('battery_entry', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='category_trash.BatteryEntry')),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adressen',
            },
            bases=('geomodels.address',),
        ),
    ]

# Generated by Django 3.0 on 2020-01-29 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category_trash', '0009_auto_20200116_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addressbatteryentry',
            options={'verbose_name_plural': 'Adresse'},
        ),
        migrations.AlterModelOptions(
            name='addressclothingentry',
            options={'verbose_name_plural': 'Adresse'},
        ),
        migrations.AlterModelOptions(
            name='addresselectroentry',
            options={'verbose_name_plural': 'Adresse'},
        ),
        migrations.AlterModelOptions(
            name='addressglassentry',
            options={'verbose_name_plural': 'Adresse'},
        ),
        migrations.AlterModelOptions(
            name='addressilluminantentry',
            options={'verbose_name_plural': 'Adresse'},
        ),
        migrations.AlterModelOptions(
            name='addressrecyclingcentreentry',
            options={'verbose_name_plural': 'Adresse'},
        ),
        migrations.AlterModelOptions(
            name='openinghoursglassentry',
            options={'verbose_name_plural': 'Öffnungszeiten'},
        ),
        migrations.AlterField(
            model_name='addressbatteryentry',
            name='battery_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_trash.BatteryEntry'),
        ),
        migrations.AlterField(
            model_name='addressclothingentry',
            name='clothing_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_trash.ClothingEntry'),
        ),
        migrations.AlterField(
            model_name='addresselectroentry',
            name='electro_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_trash.ElectroEntry'),
        ),
        migrations.AlterField(
            model_name='addressglassentry',
            name='glass_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_trash.GlassEntry'),
        ),
        migrations.AlterField(
            model_name='addressilluminantentry',
            name='illuminant_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_trash.IlluminantEntry'),
        ),
        migrations.AlterField(
            model_name='addressrecyclingcentreentry',
            name='recyclingcentre_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_trash.RecyclingcentreEntry'),
        ),
        migrations.AlterField(
            model_name='openinghoursbatteryentry',
            name='battery_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_trash.BatteryEntry'),
        ),
        migrations.AlterField(
            model_name='openinghoursclothingentry',
            name='clothing_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_trash.ClothingEntry'),
        ),
        migrations.AlterField(
            model_name='openinghourselectroentry',
            name='electro_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_trash.ElectroEntry'),
        ),
        migrations.AlterField(
            model_name='openinghoursglassentry',
            name='glass_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_trash.GlassEntry'),
        ),
        migrations.AlterField(
            model_name='openinghoursilluminantentry',
            name='illuminant_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_trash.IlluminantEntry'),
        ),
        migrations.AlterField(
            model_name='openinghoursrecyclingcentreentry',
            name='recyclingcentre_entry',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category_trash.RecyclingcentreEntry'),
        ),
    ]

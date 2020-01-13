# Generated by Django 3.0 on 2020-01-13 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geomodels', '0011_openinghours'),
        ('category_trash', '0005_auto_20200112_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openinghoursbatteryentry',
            options={},
        ),
        migrations.AlterModelOptions(
            name='openinghoursclothingentry',
            options={},
        ),
        migrations.AlterModelOptions(
            name='openinghourselectroentry',
            options={},
        ),
        migrations.AlterModelOptions(
            name='openinghoursglassentry',
            options={},
        ),
        migrations.AlterModelOptions(
            name='openinghoursrecyclingcentreentry',
            options={},
        ),
        migrations.RemoveField(
            model_name='openinghoursbatteryentry',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='openinghoursbatteryentry',
            name='id',
        ),
        migrations.RemoveField(
            model_name='openinghoursbatteryentry',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='openinghoursbatteryentry',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='openinghoursbatteryentry',
            name='sunday',
        ),
        migrations.RemoveField(
            model_name='openinghoursbatteryentry',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='openinghoursbatteryentry',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='openinghoursbatteryentry',
            name='wednesday',
        ),
        migrations.RemoveField(
            model_name='openinghoursclothingentry',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='openinghoursclothingentry',
            name='id',
        ),
        migrations.RemoveField(
            model_name='openinghoursclothingentry',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='openinghoursclothingentry',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='openinghoursclothingentry',
            name='sunday',
        ),
        migrations.RemoveField(
            model_name='openinghoursclothingentry',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='openinghoursclothingentry',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='openinghoursclothingentry',
            name='wednesday',
        ),
        migrations.RemoveField(
            model_name='openinghourselectroentry',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='openinghourselectroentry',
            name='id',
        ),
        migrations.RemoveField(
            model_name='openinghourselectroentry',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='openinghourselectroentry',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='openinghourselectroentry',
            name='sunday',
        ),
        migrations.RemoveField(
            model_name='openinghourselectroentry',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='openinghourselectroentry',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='openinghourselectroentry',
            name='wednesday',
        ),
        migrations.RemoveField(
            model_name='openinghoursglassentry',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='openinghoursglassentry',
            name='id',
        ),
        migrations.RemoveField(
            model_name='openinghoursglassentry',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='openinghoursglassentry',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='openinghoursglassentry',
            name='sunday',
        ),
        migrations.RemoveField(
            model_name='openinghoursglassentry',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='openinghoursglassentry',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='openinghoursglassentry',
            name='wednesday',
        ),
        migrations.RemoveField(
            model_name='openinghoursilluminantentry',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='openinghoursilluminantentry',
            name='id',
        ),
        migrations.RemoveField(
            model_name='openinghoursilluminantentry',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='openinghoursilluminantentry',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='openinghoursilluminantentry',
            name='sunday',
        ),
        migrations.RemoveField(
            model_name='openinghoursilluminantentry',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='openinghoursilluminantentry',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='openinghoursilluminantentry',
            name='wednesday',
        ),
        migrations.RemoveField(
            model_name='openinghoursrecyclingcentreentry',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='openinghoursrecyclingcentreentry',
            name='id',
        ),
        migrations.RemoveField(
            model_name='openinghoursrecyclingcentreentry',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='openinghoursrecyclingcentreentry',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='openinghoursrecyclingcentreentry',
            name='sunday',
        ),
        migrations.RemoveField(
            model_name='openinghoursrecyclingcentreentry',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='openinghoursrecyclingcentreentry',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='openinghoursrecyclingcentreentry',
            name='wednesday',
        ),
        migrations.AddField(
            model_name='openinghoursbatteryentry',
            name='openinghours_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.OpeningHours'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='openinghoursclothingentry',
            name='openinghours_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.OpeningHours'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='openinghourselectroentry',
            name='openinghours_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.OpeningHours'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='openinghoursglassentry',
            name='openinghours_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.OpeningHours'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='openinghoursilluminantentry',
            name='openinghours_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.OpeningHours'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='openinghoursrecyclingcentreentry',
            name='openinghours_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geomodels.OpeningHours'),
            preserve_default=False,
        ),
    ]

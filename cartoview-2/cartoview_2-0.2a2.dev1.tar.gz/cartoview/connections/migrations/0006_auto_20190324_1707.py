# Generated by Django 2.1.3 on 2019-03-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0005_auto_20190324_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='server_type',
            field=models.CharField(choices=[('ESRI', 'ArcGIS Server'), ('MS', 'MapServer'), ('GS', 'Geoserver'), ('GEOJSON', 'GeoJSON')], help_text='Server Type', max_length=15),
        ),
    ]

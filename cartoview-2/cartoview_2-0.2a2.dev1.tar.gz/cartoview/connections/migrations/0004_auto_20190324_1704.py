# Generated by Django 2.1.3 on 2019-03-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0003_auto_20190323_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='resources_type',
            field=models.CharField(choices=[('wms', 'Web Map Service'), ('wfs', 'Web Feature Service'), ('geojson', 'GeoJSON')], help_text='Resources Type', max_length=50),
        ),
        migrations.AlterField(
            model_name='server',
            name='server_type',
            field=models.CharField(choices=[('ESRI', 'ArcGIS Server'), ('MS', 'MapServer'), ('GS', 'Geoserver'), ('SL', 'Single Layer')], help_text='Server Type', max_length=5),
        ),
    ]

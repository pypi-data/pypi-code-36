# Generated by Django 2.1.5 on 2019-04-10 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_endpoint', '0007_auto_20190410_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='providerendpoint',
            old_name='ppd',
            new_name='ppi',
        ),
    ]

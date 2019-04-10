# Generated by Django 2.1.5 on 2019-04-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_endpoint', '0006_auto_20190130_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerendpoint',
            name='ppd',
            field=models.BooleanField(default=False, help_text='put callerid in SIP P-Prefered-Id field if enabled', verbose_name='caller ID in PPD field'),
        ),
        migrations.AddField(
            model_name='providerendpoint',
            name='ppd',
            field=models.BooleanField(default=False, help_text='put callerid in SIP P-Prefered-Id field if enabled', verbose_name='caller ID in PPD field'),
        ),
    ]

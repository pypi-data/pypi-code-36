# Generated by Django 2.1.4 on 2018-12-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_endpoint', '0002_auto_20181218_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codec',
            name='description',
            field=models.TextField(blank=True, max_length=100, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='codec',
            name='number',
            field=models.PositiveIntegerField(help_text='payload types (PT) for audio encodings', unique=True, verbose_name='payload number'),
        ),
        migrations.AlterField(
            model_name='codec',
            name='ptime',
            field=models.PositiveIntegerField(verbose_name='ptime'),
        ),
        migrations.AlterField(
            model_name='codec',
            name='rfc_name',
            field=models.CharField(help_text='format is important !.', max_length=30, unique=True, verbose_name='rfc name'),
        ),
        migrations.AlterField(
            model_name='codec',
            name='stereo',
            field=models.BooleanField(default=False, verbose_name='is stereo ?'),
        ),
        migrations.AlterField(
            model_name='customerendpoint',
            name='codec_list',
            field=models.ManyToManyField(blank=True, null=True, related_name='codecs_c', to='pyfb_endpoint.Codec'),
        ),
        migrations.AlterField(
            model_name='providerendpoint',
            name='codec_list',
            field=models.ManyToManyField(blank=True, null=True, related_name='codecs_p', to='pyfb_endpoint.Codec'),
        ),
    ]

# Generated by Django 2.1.5 on 2019-04-08 18:45

import django.core.validators
from django.db import migrations, models
import ls.joyous.utils.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('joyous', '0014_auto_20190328_0652'),
    ]

    operations = [
        migrations.CreateModel(
            name='RescheduleMultidayEventPage',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'postponements',
                'proxy': True,
                'verbose_name': 'postponement',
            },
            bases=(ls.joyous.utils.mixins.ProxyPageMixin, 'joyous.postponementpage'),
        ),
        migrations.RemoveField(
            model_name='postponementpage',
            name='group_page',
        ),
        migrations.RemoveField(
            model_name='postponementpage',
            name='uid',
        ),
        migrations.AddField(
            model_name='postponementpage',
            name='num_days',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)], verbose_name='number of days'),
        ),
        migrations.DeleteModel(
            name='MultidayRecurringEventPage',
        ),
        migrations.CreateModel(
            name='MultidayRecurringEventPage',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'multiday recurring event pages',
                'proxy': True,
                'verbose_name': 'multiday recurring event page',
            },
            bases=(ls.joyous.utils.mixins.ProxyPageMixin, 'joyous.recurringeventpage'),
        ),
    ]

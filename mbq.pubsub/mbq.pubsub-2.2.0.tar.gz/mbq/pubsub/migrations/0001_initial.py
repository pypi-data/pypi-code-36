# Generated by Django 2.1.5 on 2019-01-11 22:34

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UndeliverableMessage",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("message_type", models.CharField(max_length=256)),
                ("message_timestamp", models.DateTimeField()),
                ("payload", models.TextField()),
                ("queue", models.CharField(max_length=80)),
                ("topic_arn", models.CharField(max_length=2048, null=True)),
            ],
        )
    ]

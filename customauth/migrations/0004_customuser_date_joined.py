# Generated by Django 5.0.2 on 2024-04-01 18:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customauth", "0003_remove_userprofile_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hero_crafter", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="character",
            name="biography",
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-02 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hero_crafter", "0003_character_portrait_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="portrait_url",
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]

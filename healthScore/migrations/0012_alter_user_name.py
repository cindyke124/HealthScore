# Generated by Django 4.2 on 2024-03-09 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("healthScore", "0011_alter_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.TextField(blank=True, default="", max_length=255),
        ),
    ]

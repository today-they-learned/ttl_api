# Generated by Django 3.2.11 on 2022-02-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0008_grass"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="grass",
            name="created_at",
        ),
        migrations.AddField(
            model_name="grass",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]

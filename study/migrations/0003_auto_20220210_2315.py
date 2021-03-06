# Generated by Django 3.2.11 on 2022-02-10 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("study", "0002_alter_study_studied_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="study",
            name="count",
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name="study",
            name="studied_at",
        ),
        migrations.AddField(
            model_name="study",
            name="studied_at",
            field=models.DateField(auto_now_add=True, verbose_name="studied at"),
        ),
    ]

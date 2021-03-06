# Generated by Django 4.0.2 on 2022-02-12 12:56

import article.models.upload_image
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0012_article_feedback_count"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="uploads/"),
                ),
            ],
            options={
                "verbose_name": "UploadImage",
                "verbose_name_plural": "UploadImages",
                "db_table": "upload_images",
            },
        ),
    ]

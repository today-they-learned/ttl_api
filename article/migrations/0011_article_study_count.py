# Generated by Django 3.2.11 on 2022-02-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_article_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='study_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 3.2 on 2022-01-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220123_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookaccount',
            name='username',
            field=models.TextField(blank=True, null=True, verbose_name='sns username'),
        ),
        migrations.AlterField(
            model_name='instagramaccount',
            name='username',
            field=models.TextField(blank=True, null=True, verbose_name='sns username'),
        ),
        migrations.AlterField(
            model_name='twitteraccount',
            name='username',
            field=models.TextField(blank=True, null=True, verbose_name='sns username'),
        ),
    ]

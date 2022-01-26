# Generated by Django 3.2 on 2022-01-23 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220123_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(verbose_name='username')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='twitter_account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'TwitterAccount',
                'verbose_name_plural': 'TwitterAccounts',
                'db_table': 'twitter_accounts',
                'default_related_name': 'twitter_account',
            },
        ),
        migrations.CreateModel(
            name='InstagramAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(verbose_name='username')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instagram_account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'InstagramAccount',
                'verbose_name_plural': 'InstagramAccounts',
                'db_table': 'instagram_accounts',
                'default_related_name': 'instagram_account',
            },
        ),
        migrations.CreateModel(
            name='FacebookAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(verbose_name='username')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='facebook_account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'FacebookAccount',
                'verbose_name_plural': 'FacebookAccounts',
                'db_table': 'facebook_accounts',
                'default_related_name': 'facebook_account',
            },
        ),
    ]
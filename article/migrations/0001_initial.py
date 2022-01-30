# Generated by Django 3.2 on 2022-01-26 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('source', models.CharField(choices=[('tl', 'TTL'), ('vl', 'Velog'), ('gh', 'Github'), ('ts', 'Tistory')], default='tl', max_length=2, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='article/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to=settings.AUTH_USER_MODEL, verbose_name='writer')),
            ],
        ),
    ]

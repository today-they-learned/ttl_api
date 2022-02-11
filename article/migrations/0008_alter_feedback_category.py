# Generated by Django 3.2.11 on 2022-02-11 11:23

import article.models.feedback
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_feedback_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='category',
            field=models.CharField(choices=[('thumbs_up', 'thumbs_up'), ('heart', 'heart'), ('clap', 'clap'), ('lion', 'lion'), ('thinking', 'thinking'), ('smile', 'smile'), ('clover', 'clover'), ('eyes', 'eyes'), ('perfect', 'perfect'), ('bulb', 'bulb')], default='thumbs_up', max_length=10,),
        ),
    ]

# Generated by Django 3.1.7 on 2021-02-25 16:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

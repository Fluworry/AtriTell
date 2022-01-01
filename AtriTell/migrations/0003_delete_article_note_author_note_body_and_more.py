# Generated by Django 4.0 on 2022-01-01 19:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('AtriTell', '0002_article_random_url_id_alter_article_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='note',
            name='author',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='note',
            name='body',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='creation_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='random_url_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default=datetime.datetime(2022, 1, 1, 19, 42, 54, 73560, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
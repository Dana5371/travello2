# Generated by Django 3.1 on 2021-11-16 06:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_auto_20211116_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ikes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]

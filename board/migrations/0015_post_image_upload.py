# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-22 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_auto_20180916_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_upload',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
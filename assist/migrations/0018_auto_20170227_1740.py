# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assist', '0017_auto_20170227_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='files',
            field=models.FileField(upload_to='/'),
        ),
        migrations.AlterField(
            model_name='exampaper',
            name='files',
            field=models.FileField(upload_to='/'),
        ),
        migrations.AlterField(
            model_name='material',
            name='files',
            field=models.FileField(upload_to='/'),
        ),
    ]

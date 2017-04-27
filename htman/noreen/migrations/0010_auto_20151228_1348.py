# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0009_auto_20151228_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='article',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AlterField(
            model_name='img',
            name='title',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]

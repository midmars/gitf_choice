# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0013_auto_20151229_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='result_anxiety',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='member',
            name='result_depresion',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='member',
            name='result_edge',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]

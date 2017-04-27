# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0004_auto_20151227_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='title',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]

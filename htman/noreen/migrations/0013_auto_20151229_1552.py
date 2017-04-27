# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0012_auto_20151228_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='level_result',
        ),
        migrations.RemoveField(
            model_name='member',
            name='test_result',
        ),
    ]

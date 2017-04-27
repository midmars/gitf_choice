# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0006_auto_20151227_2352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='img',
            old_name='article',
            new_name='a1',
        ),
        migrations.RenameField(
            model_name='img',
            old_name='title',
            new_name='t1',
        ),
    ]

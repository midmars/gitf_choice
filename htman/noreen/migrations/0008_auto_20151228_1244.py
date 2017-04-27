# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0007_auto_20151228_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='img',
            old_name='t1',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='img',
            old_name='a1',
            new_name='title',
        ),
    ]

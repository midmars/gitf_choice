# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0014_auto_20151229_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='result_depresion',
            new_name='result_depression',
        ),
    ]

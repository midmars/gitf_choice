# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0003_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='finsh',
            new_name='finish',
        ),
    ]

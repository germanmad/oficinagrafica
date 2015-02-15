# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0003_work_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

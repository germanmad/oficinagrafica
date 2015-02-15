# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 12, 30, 40, 443000, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]

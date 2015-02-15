# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0004_auto_20150212_1458'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='work',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='work',
            name='year_in_school',
            field=models.CharField(default=b'SW', max_length=2, choices=[(b'SW', b'Freshman'), (b'IC', b'Sophomore'), (b'DG', b'Diseno Grafico'), (b'IL', b'Junior'), (b'3D', b'Diseno 3D')]),
            preserve_default=True,
        ),
    ]

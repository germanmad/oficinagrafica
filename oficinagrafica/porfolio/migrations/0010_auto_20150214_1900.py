# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0009_auto_20150214_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='category',
            field=models.CharField(default=b'SITIOS', max_length=30, choices=[(b'SITIOS', b'Sitios Web'), (b'IDENTIDAD', b'Identidad Corporativa'), (b'GRAFICO', b'Diseno Gr\xc3\xa1fico'), (b'ILUSTRACION', b'Ilustraci\xc3\xb3n'), (b'3D', b'Dise\xc3\xb1o 3D')]),
            preserve_default=True,
        ),
    ]

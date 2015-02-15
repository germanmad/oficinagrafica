# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0013_auto_20150214_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='category',
            field=models.CharField(default=b'Sitios Web', max_length=30, choices=[(b'Sitios Web', b'Sitios Web'), (b'Identidad Corporativa', b'Identidad Corporativa'), (b'Dise\xc3\xb1o Gr\xc3\xa1fico', b'Dise\xc3\xb1o Gr\xc3\xa1fico'), (b'Ilustraci\xc3\xb3n', b'Ilustraci\xc3\xb3n'), (b'Dise\xc3\xb1o 3D', b'Dise\xc3\xb1o 3D')]),
            preserve_default=True,
        ),
    ]

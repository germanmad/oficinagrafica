# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0011_auto_20150214_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='category',
            field=models.CharField(default=b'Sitios Web', max_length=30, choices=[(b'Sitios Web', b'Sitios Web'), (b'Identidad Corporativa', b'Identidad Corporativa'), (b'<p>Dise\xc3\xb1o Gr\xc3\xa1fico</p>', b'Diseno Gr\xc3\xa1fico'), (b'Ilustracion', b'Ilustraci\xc3\xb3n'), (b'Diseno 3D', b'Dise\xc3\xb1o 3D')]),
            preserve_default=True,
        ),
    ]

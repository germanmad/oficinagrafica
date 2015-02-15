# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0007_auto_20150214_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='category',
            field=models.CharField(default=b'Sitios Web', max_length=30, choices=[(b'Sitios Web', b'Sitios Web'), (b'Identidad Corporativa', b'Identidad Corporativa'), (b'Diseno Gr&aacute;fico', b'Diseno Grafico'), (b'Ilustraci\xf3n', b'Ilustraci\xf3n'), (b'Dise&ntilde;o 3D', b'Dise&ntilde;o 3D')]),
            preserve_default=True,
        ),
    ]

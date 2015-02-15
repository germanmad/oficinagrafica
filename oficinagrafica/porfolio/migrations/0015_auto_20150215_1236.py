# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0014_auto_20150214_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='category',
            field=models.CharField(default=b'Sitios Web', max_length=30, choices=[(b'Sitios Web', b'SW'), (b'Identidad Corporativa', b'IC'), (b'Dise\xc3\xb1o Gr\xc3\xa1fico', b'DG'), (b'Ilustraci\xc3\xb3n', b'IL'), (b'Dise\xc3\xb1o 3D', b'D3')]),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0005_auto_20150214_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='work',
            name='category',
            field=models.CharField(default=b'SW', max_length=2, choices=[(b'SW', b'Sitios Web'), (b'IC', b'Identidad Corporativa'), (b'DG', b'Diseno Gr&aacute;fico'), (b'IL', b'Ilustraci&oacute;n'), (b'3D', b'Dise&ntilde;o 3D')]),
            preserve_default=True,
        ),
    ]

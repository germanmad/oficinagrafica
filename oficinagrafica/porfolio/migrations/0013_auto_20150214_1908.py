# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0012_auto_20150214_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='category',
            field=models.CharField(default=b'SitiosWeb', max_length=30, choices=[(b'SitiosWeb', b'Sitios Web'), (b'IdentidadCorporativa', b'Identidad Corporativa'), (b'<p>DisenoGrafico</p>', b'Dise\xc3\xb1o Gr\xc3\xa1fico'), (b'Ilustracion', b'Ilustraci\xc3\xb3n'), (b'Diseno3D', b'Dise\xc3\xb1o 3D')]),
            preserve_default=True,
        ),
    ]

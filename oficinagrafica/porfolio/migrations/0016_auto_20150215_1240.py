# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0015_auto_20150215_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='category',
            field=models.CharField(default='Sitios Web', max_length=30, choices=[('Sitios Web', 'SW'), ('Identidad Corporativa', 'IC'), ('Dise\xf1o Gr\xe1fico', 'DG'), ('Ilustraci\xf3n', 'IL'), ('Dise\xf1o 3D', 'D3')]),
            preserve_default=True,
        ),
    ]

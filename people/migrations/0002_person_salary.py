# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='salary',
            field=models.IntegerField(default=datetime.datetime(2016, 4, 3, 15, 36, 2, 464000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

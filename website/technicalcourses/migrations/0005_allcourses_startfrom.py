# Generated by Django 3.0.3 on 2020-08-15 17:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('technicalcourses', '0004_remove_allcourses_startfrom'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcourses',
            name='startFrom',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 15, 17, 55, 35, 653346, tzinfo=utc), verbose_name='start from'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.6 on 2022-08-31 00:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='loan_approved_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 8, 31, 0, 52, 43, 20163, tzinfo=utc)),
        ),
    ]

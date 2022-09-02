# Generated by Django 4.0.6 on 2022-09-01 19:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0007_prestamos_id_cuenta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestamos',
            name='id_cuenta',
        ),
        migrations.AlterField(
            model_name='prestamos',
            name='loan_approved_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 9, 1, 19, 4, 6, 898356, tzinfo=utc)),
        ),
    ]
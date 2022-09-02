# Generated by Django 4.0.6 on 2022-08-31 00:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0003_remove_prestamos_id_sucursal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamos',
            name='id_sucursal',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='prestamos',
            name='loan_approved_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 8, 31, 0, 54, 1, 231728, tzinfo=utc)),
        ),
    ]

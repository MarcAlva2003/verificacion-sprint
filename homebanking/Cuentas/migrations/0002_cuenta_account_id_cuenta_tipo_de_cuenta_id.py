# Generated by Django 4.0.6 on 2022-08-26 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='account_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='tipo_de_cuenta_id',
            field=models.IntegerField(null=True),
        ),
    ]
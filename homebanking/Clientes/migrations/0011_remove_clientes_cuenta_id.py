# Generated by Django 4.0.6 on 2022-08-25 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0010_clientes_cuenta_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='cuenta_id',
        ),
    ]

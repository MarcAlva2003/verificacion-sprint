# Generated by Django 4.0.6 on 2022-08-31 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0003_remove_cuenta_account_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuenta',
            options={'ordering': ('-customer_id',), 'verbose_name': 'Cuenta', 'verbose_name_plural': 'Cuentas'},
        ),
    ]
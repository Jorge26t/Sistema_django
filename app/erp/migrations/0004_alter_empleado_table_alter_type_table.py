# Generated by Django 4.1.1 on 2022-09-14 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_type_alter_empleado_table_empleado_type'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='empleado',
            table='Empleado',
        ),
        migrations.AlterModelTable(
            name='type',
            table='Tipo',
        ),
    ]

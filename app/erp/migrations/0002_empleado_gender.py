# Generated by Django 4.1.1 on 2022-09-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='gender',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
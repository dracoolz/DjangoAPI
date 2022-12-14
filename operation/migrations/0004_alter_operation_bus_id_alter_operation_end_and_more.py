# Generated by Django 4.0.1 on 2022-12-01 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0005_alter_buses_name'),
        ('operation', '0003_alter_operation_bus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='bus_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buses.buses', unique=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='end',
            field=models.BooleanField(unique=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='start',
            field=models.BooleanField(unique=True),
        ),
    ]

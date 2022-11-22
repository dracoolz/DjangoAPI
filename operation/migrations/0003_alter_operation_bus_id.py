# Generated by Django 4.0.1 on 2022-11-22 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0004_alter_buses_group_id'),
        ('operation', '0002_alter_operation_bus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='bus_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buses.buses'),
        ),
    ]
# Generated by Django 4.0.1 on 2023-01-18 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_remove_groups_buses_id_groups_bus_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groups',
            old_name='bus_id',
            new_name='bus',
        ),
    ]

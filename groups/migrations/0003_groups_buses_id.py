# Generated by Django 4.0.1 on 2023-01-10 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0007_remove_buses_group_id'),
        ('groups', '0002_alter_groups_address_alter_groups_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='buses_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='buses.buses'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-12-08 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_alter_operation_bus_id'),
        ('users', '0012_alter_users_driver_alter_users_email'),
        ('passenger', '0004_alter_passenger_operation_id_alter_passenger_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='operation_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='operation.operation', unique=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='user_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.users', unique=True),
        ),
    ]

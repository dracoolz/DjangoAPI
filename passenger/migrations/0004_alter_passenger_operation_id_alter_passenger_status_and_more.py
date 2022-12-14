# Generated by Django 4.0.1 on 2022-12-01 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_users_driver_alter_users_email'),
        ('operation', '0004_alter_operation_bus_id_alter_operation_end_and_more'),
        ('passenger', '0003_alter_passenger_operation_id_alter_passenger_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='operation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operation.operation', unique=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='status',
            field=models.BooleanField(unique=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users', unique=True),
        ),
    ]

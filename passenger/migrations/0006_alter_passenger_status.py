# Generated by Django 4.0.1 on 2023-01-04 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0005_alter_passenger_operation_id_alter_passenger_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='status',
            field=models.BooleanField(),
        ),
    ]

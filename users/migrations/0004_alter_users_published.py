# Generated by Django 4.0.4 on 2022-10-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_driver_alter_users_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
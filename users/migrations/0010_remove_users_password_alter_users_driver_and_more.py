# Generated by Django 4.0.1 on 2022-11-22 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_users_family_id_alter_users_group_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
        migrations.AlterField(
            model_name='users',
            name='driver',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]
# Generated by Django 4.0.4 on 2022-10-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_buses_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='buses_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=200)),
                ('busId', models.IntegerField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('driver', models.BooleanField()),
                ('serial_number', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
# Generated by Django 4.0.4 on 2022-10-20 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=200)),
                ('driver', models.CharField(default='', max_length=200)),
                ('serial_number', models.IntegerField(default='')),
                ('published', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
    ]
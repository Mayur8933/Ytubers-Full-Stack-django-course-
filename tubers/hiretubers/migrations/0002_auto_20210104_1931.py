# Generated by Django 3.1.4 on 2021-01-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='user_id',
            field=models.BigIntegerField(),
        ),
    ]
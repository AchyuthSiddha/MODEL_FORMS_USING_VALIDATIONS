# Generated by Django 4.1.4 on 2023-04-26 12:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sid',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxLengthValidator(5)]),
        ),
    ]

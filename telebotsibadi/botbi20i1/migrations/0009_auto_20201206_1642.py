# Generated by Django 3.1.2 on 2020-12-06 10:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botbi20i1', '0008_auto_20201206_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rating',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]

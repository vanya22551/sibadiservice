# Generated by Django 3.1.2 on 2020-12-06 10:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botbi20i1', '0005_auto_20201206_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]

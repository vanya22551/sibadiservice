# Generated by Django 3.1.2 on 2020-11-20 20:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botbi20i1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rating_1KT',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='student',
            name='rating_2KT',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='student',
            name='rating_3KT',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
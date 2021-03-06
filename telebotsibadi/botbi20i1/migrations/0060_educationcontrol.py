# Generated by Django 3.1.7 on 2021-03-17 16:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botbi20i1', '0059_laboratory_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default=1)),
                ('weight', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100.0)])),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2021-01-06 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botbi20i1', '0028_auto_20210106_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-28 17:51

import botbi20i1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botbi20i1', '0065_laboratory_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_dir',
            field=models.FileField(blank=True, default=None, upload_to=botbi20i1.models.folder_path),
        ),
    ]

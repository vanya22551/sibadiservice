# Generated by Django 3.1.6 on 2021-03-06 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boTtelegramm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Фото'),
        ),
    ]

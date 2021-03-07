from django.db import models
from datetime import date

class Group (models.Model):
    name = models.CharField(max_length=50, verbose_name='Название группы')
    group = models.CharField(max_length=50, verbose_name='Группа')
    def __str__(self):
        return self.name

class News (models.Model):
    text = models.CharField(max_length=1250, 
                            blank=True,
                            verbose_name='Текст')
    photo = models.CharField(blank=True, max_length=250, verbose_name='Фото')
    File = models.CharField(blank=True, max_length=50, verbose_name='Файл')
    group = models.ForeignKey(Group, blank=True, default='', on_delete=models.CASCADE)
    Date = models.DateField(auto_now=True)

    def __str__(self):
        return 'Новость ' + str(self.pk)

# Create your models here.

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.urls import reverse


class Group(models.Model):
    name = models.CharField(max_length=20,
                            default="")
    course = models.CharField(max_length=20,
                              default="")

    def __str__(self):
        return self.name


class Laboratory(models.Model):
    description = models.TextField(default="",
                                     verbose_name="Описание")
    name = models.CharField(max_length=200,
                            default="", verbose_name="Название")
    kt = models.PositiveIntegerField(default=1,
                                     verbose_name="КТ")

    group_id = models.ForeignKey(Group,
                                on_delete=models.CASCADE,
                                 default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





class Teacher(models.Model):
    second_name = models.CharField(max_length=50,
                             default="")
    name = models.CharField(max_length=50,
                            default="")                                   
    patronymic = models.CharField(max_length=50,
                            default="")                                  
    phone = models.CharField(max_length=50,
                            default="")
    email = models.CharField(max_length=50,
                            default="")
    additional_information = models.CharField(max_length=200, 
                            default="")                       
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True)
    

    def __str__(self):
        return self.second_name + " " + self.name + " " + self.patronymic

class Student(models.Model):
    group_id = models.ForeignKey(Group,
                                 on_delete=models.CASCADE,
                                 default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    personal_number = models.CharField(max_length=20,
                                       default="")
    second_name = models.CharField(max_length=50,
                             default="")
    name = models.CharField(max_length=50,
                            default="")                                   
    patronymic = models.CharField(max_length=50,
                            default="")                                  
    phone = models.CharField(max_length=50,
                            default="")
    email = models.CharField(max_length=50,
                            default="")
    git_hub = models.CharField(max_length=100,
                               default="")
    rating_1KT = models.FloatField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100.00)])
    rating_2KT = models.FloatField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100.00)])
    rating_3KT = models.FloatField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100.00)])
    rating = models.FloatField(default=0,
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(100.00)])
    labs = models.ManyToManyField(Laboratory,
                                  through='Stats')

    def __str__(self):
        return self.second_name + " " + self.name + " " + self.patronymic


class File(models.Model):
    file = models.FileField()

    lab = models.ForeignKey(Laboratory, blank=True,
                            on_delete=models.CASCADE)
    student = models.ForeignKey(Student, blank=True,
                                on_delete=models.CASCADE )

    def __str__(self):
        return self.student.name + " " + self.lab.name + " " + self.file.name


class Hint(models.Model):
    text = models.TextField(default="")
    lab = models.ForeignKey(Laboratory,
                            on_delete=models.CASCADE,
                            null=True)

    def __str__(self):
        return self.text


class Stats(models.Model):
    lab = models.ForeignKey(Laboratory,
                            on_delete=models.CASCADE)
    student = models.ForeignKey(Student,
                                on_delete=models.CASCADE)
    
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.lab.name + " " + self.student.name

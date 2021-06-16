from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.urls import reverse

def folder_path(instance, filename):
    return "{0}/{1}".format(instance.personal_number, filename)

def folder_path_fileIn(instance, filename):
    return "{0}/input/{1}".format(instance.name, filename)

def folder_path_fileOut(instance, filename):
    return "{0}/output/{1}".format(instance.name, filename)

"""
    Преподователь, информация о нем
"""
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


"""
    Группы
"""
class Group(models.Model):
    name = models.CharField(max_length=20,
                            default="")
    course = models.CharField(max_length=20,
                              default="")
    teacher = models.ForeignKey(Teacher, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


"""
    Лаборантоные работы
"""
class Laboratory(models.Model):

    name = models.CharField(max_length=200,
                            default="", verbose_name="Название")
    description = models.TextField(default="",
                                     verbose_name="Описание")
    kt = models.PositiveIntegerField(default=1,
                                     verbose_name="КТ")

    comment = models.TextField(default="", blank=True, verbose_name="Комментарий преподователя")

    group_id = models.ForeignKey(Group,
                                on_delete=models.CASCADE,
                                 default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    weight = models.FloatField(default=0,  
                                validators=[MinValueValidator(0),
                                               MaxValueValidator(100.00)],
                                blank=True,
                                verbose_name="Вес лабы (%)")
    file_input = models.FileField(upload_to= folder_path_fileIn, default= None, blank=True)

    file_output = models.FileField(upload_to= folder_path_fileOut, default= None, blank=True)

    def __str__(self):
        return self.name



"""
    Студент, вся информация о нем, рейтинги
"""
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
                                           MaxValueValidator(100.00)], )
    labs = models.ManyToManyField(Laboratory,
                                  through='Stats')

    student_dir = models.FileField(upload_to= folder_path, default= None, blank=True)

    def save(self, *args, **kwargs):
        self.rating = round(self.rating, 2)
        self.rating_1KT = round(self.rating_1KT, 2)
        self.rating_2KT = round(self.rating_2KT, 2)
        self.rating_3KT = round(self.rating_3KT, 2)
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.second_name + " " + self.name + " " + self.patronymic


"""
    Файлы, которые студент отправляет на проверку
"""
class File(models.Model):
    file = models.FileField()

    lab = models.ForeignKey(Laboratory, blank=True,
                            on_delete=models.CASCADE)
    student = models.ForeignKey(Student, blank=True,
                                on_delete=models.CASCADE )

    def __str__(self):
        return self.student.name + " " + self.lab.name + " " + self.file.name


"""
    Подсказки, связаны с лабой
"""
class Hint(models.Model):
    text = models.TextField(default="")
    lab = models.ForeignKey(Laboratory,
                            on_delete=models.CASCADE,
                            null=True)

    def __str__(self):
        return self.text


"""
    Контольные точки, можно задать вес и связать с группой
"""
class EducationControl(models.Model):

    KT =  [
        (1, (1)),
        (2, (2)),
        (3, (3)),
    ]
    number = models.IntegerField(default="1", choices=KT, verbose_name='Номер КТ')
    weight = models.IntegerField(default=0, validators=[MinValueValidator(0),
                                            MaxValueValidator(100.00)], verbose_name="Вес КТ (%)")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=1,  verbose_name="Группа")

    def __str__(self):
        return self.group.name + " KT№ " + str(self.number) 


"""
    Статистика, лабараторные привязываются к каждому студенту, имеют статус(true/false)
"""
class Stats(models.Model):
    lab = models.ForeignKey(Laboratory,
                            on_delete=models.CASCADE)
    student = models.ForeignKey(Student,
                                on_delete=models.CASCADE)
    
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.lab.name + " " + self.student.name

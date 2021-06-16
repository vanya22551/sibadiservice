from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User


from .models import Student, Hint, Stats, Group, Laboratory, File, Teacher, EducationControl
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from .forms import LabForm, AuthUserForm, RegisterUserForm, ChangePasswordForm, FileForm, EditTeacherInformationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import update_session_auth_hash
'''
import sys
import os
import subprocess
import shutil
import pathlib
from pathlib import Path
import os.path
import argparse
'''

'''

def open_code(request, res_file, check_file, student_name, lab_numb, lab_exp):
    """
    res_file - ссылка на дерикторию, где лежат входные и выходные данные проверки
    check_file - ссылка на личную аудиторию студента
    student_name - имя студента
    lub_num - номер лыбы
    lab_exp - расширение файла
    """

    #parser = argparse.ArgumentParser(description='enter the key directories')
    #parser.add_argument('res', type=str, help='enter the directory with the files to res')
    #parser.add_argument('files_student', type=str, help='enter the directory with the students file')
    #parser.add_argument('last_name', type=str, help='enter the students last name')
    #parser.add_argument('lab_number', type=str, help='enter the lab number')
    #parser.add_argument('lab_expansion', type=str, help='enter the extension')
    #args = parser.parse_args()

    #a = settings.BASE_DIR
    main = settings.BASE_DIR

    resFile = os.path.join(res_file)

    checkFile = os.path.join(check_file)

    studentName = os.path.join(student_name)

    labNum = os.path.join(lab_numb)

    labExp = os.path.join(lab_exp)

    #name_files = (args.last_name + '_' + args.lab_number + args.lab_expansion)

    #files_student = os.path.join(args.files_student, name_files)

    files_copy1 = os.path.join(checkFile,'input.in.txt')

    files_copy2 = os.path.join(checkFile,'input.secret.txt')

    files_insert = os.path.join(main,'input.txt')

#
#
#    def Checking_Hashes1(check,main):
#        f = open(os.path.join(res_file, 'output.out.txt'), "r")
#        f2 = open(os.path.join(main, 'output.txt'), "r")
#        global percent
#        percent=0
#        while True:
#            answer_teacher1=hash(f.readline())
#            answer_student1=hash(f2.readline())
#    if answer_teacher1==answer_student1:
#        percent=percent+10
#    if not answer_student1:
#        break
#    f.close()
#    f2.close()
#
#    def Checking_Hashes2(check,main):
#        f = open(os.path.join(res_file, 'output.secret.txt'), "r")
#        f2 = open(os.path.join(main, 'output.txt'), "r")
#    global percent2
#    percent2=0
#    while True:
#        answer_teacher1=hash(f.readline())
#        answer_student1=hash(f2.readline())
#    if answer_teacher1==answer_student1:
#        percent2=percent2+10
#    if not answer_student1:
#        break
#    f.close()
#    f2.close()
#
#
#    shutil.copyfile(files_copy1,files_insert)
#    print ('..................copy file true.................')
#    subprocess.call([sys.executable,checkFile])
#    print ('.........................Launch file true.........................')
#    Checking_Hashes1(check,main)
#    print ('......................Checking files hashes 1 true................')
#    shutil.copyfile(files_copy2,files_insert)
#    print ('....................Copy file true..................')
#    launchFile(files_student)
#    print ('........................Launch file true..........................')
#    Checking_Hashes2(check,main)
#    print ('.........................Checking files hashes 2 true...............')
#    print ('.........................',percent+percent2,'...............')
#    os.remove(os.path.join(main,'input.txt'))
#    os.remove(os.path.join(main,'output.txt'))
#
#
'''


"""
    Функция вывода главной страницы
"""

class facePage(ListView):

    model = Student
    template_name='botbi20i1/face_page.html'
    context_object_name = 'students'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        context['teachers'] = Teacher.objects.all()
        context['stats'] = Stats.objects.all().order_by('lab')
        return context


"""
    Страница пользователя 
"""

class userPage(ListView):

    model = Student
    template_name='botbi20i1/user_page.html'
    context_object_name = 'students'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        context['teachers'] = Teacher.objects.all()
        context['stats'] = Stats.objects.all()
        return context



class LoginUserView(LoginView):
    template_name = 'botbi20i1/login_page.html'
    form_class = AuthUserForm
    success_url = 'face_page'

    def get_success_url(self):
        return self.success_url


class Logout(LogoutView):
    next_page = ''


class RegisterUserView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'botbi20i1/register_page.html'
    success_msg = 'Пользователь создан'
    success_url = 'face_page'

    def get_success_url(self):
        return self.success_url



def ChangePasswordView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ChangePasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return redirect('face_page')
        else:
            fm = ChangePasswordForm(user=request.user)

        context = {
            'form': fm
        }
        return render(request, template_name='botbi20i1/changepassword_page.html', context=context)
    else:
        return redirect('face_page')


"""
    Страница группы
"""
def group(request, group_id):
    students = Student.objects.filter(group_id__id=group_id).order_by('second_name')
    print(students)
    stats = Stats.objects.all().order_by('lab')
    teachers = Teacher.objects.all()
    KT_1 = EducationControl.objects.filter(group__id=group_id ,number=1)
    KT_2 = EducationControl.objects.filter(group__id=group_id ,number=2)
    KT_3 = EducationControl.objects.filter(group__id=group_id ,number=3)

    teachr = ''
    studnt = ''
    for teacher in teachers:
        if request.user.id == teacher.user.id:
            teachr = teacher
    for student in students:
        if request.user.id == student.user.id:
            studnt = student
    context = {
        'teachers': teachers,
        'teachr': teachr,
        'kt_1': KT_1[0],
        'kt_2': KT_2[0],
        'kt_3': KT_3[0],
        'students': students,
        'studnt': studnt,
        'stats': stats,
    }

    return render(request, template_name='botbi20i1/group_page.html', context=context)


"""
    Функция вывода страницы лабы
"""
def labsPage(request, id):

    student = Student.objects.filter(user=request.user)
    labs = Laboratory.objects.filter(pk=id)
    print(labs)
    files = File.objects.filter(student=student[0], lab=labs[0])
    print(files)
    for lab in labs:
        if lab.id == id:
            lab = lab
    if not files:
        file = ''
    else:
        file = files[0]
        
    context = {
        'labs': labs,
        'student': student,
        'file': file,
        'lab': lab
    }

    return render(request, template_name='botbi20i1/labs_page.html', context=context)


"""
    Функция вывода страницы студента с лабораторными работами (Для преподователя)
"""
def studentPage(request, id):

    student = Student.objects.filter(user_id=id)
    stats = Stats.objects.filter(student=student[0])
    files = File.objects.filter(student=student[0])
    for file in files:
        print(file.lab.name)

    if not files:
        file = ''
    else:
        files = files
        
    context = {
        'stats': stats,
        'student': student[0],

        'files': files,
   
    }

    return render(request, template_name='botbi20i1/student_page.html', context=context)



def index(request, index_id):
    data = {}
    students = Student.objects.filter(group_id__id=index_id)
    for student in students:

        data.update({str(student.personal_number): {'name': student.name, 'rating': student.rating, 'labs': {}}})
        i = 1
        labs = Stats.objects.filter(student=student, status=False).prefetch_related('lab')
        for lab in labs:
            data[str(student.personal_number)]['labs'].update({
                i: {
                    'name': lab.lab.name,
                    'description': lab.lab.description,
                    'status': int(lab.status),
                    'hints': {}
                }
            })

            hints = Hint.objects.filter(lab=lab.lab.id)
            j = 1
            for hint in hints:
                data[str(student.personal_number)]['labs'][i]['hints'].update({j: hint.text})
                j += 1
            i += 1

    return JsonResponse(data)

"""
    Функция изменения статуса лабы, при нажати на radio-button, и изменения рейтинга студента
"""
def update_changes(request):
    if request.GET:
        stats = Stats.objects.get(pk=request.GET['stats_id'])
        user = Student.objects.get(pk=stats.student.id)
        labs_kt1 = user.labs.filter(kt=1)
        labs_kt2 = user.labs.filter(kt=2)
        labs_kt3 = user.labs.filter(kt=3)
        KT_number = stats.lab.kt
        kt = EducationControl.objects.filter(number=KT_number)
        if request.GET['status'] == '1':

            if user.rating_1KT <= 100 and user.rating_2KT <= 100 and user.rating_3KT <= 100:
                if KT_number == 1:
                    for lab_kt1 in labs_kt1:
                        if lab_kt1 == stats.lab:
                            ratingPoint = (lab_kt1.weight / 100) * kt[0].weight
                            
                            if stats.status == True:
                                stats.status = False
                                stats.save()
                                if user.rating_1KT > 0:
                                    user.rating_1KT -= lab_kt1.weight
                                    user.rating -= ratingPoint
                            else:
                                stats.status = True
                                stats.save()
                                if user.rating_1KT >= 0:
                                    user.rating_1KT += lab_kt1.weight
                                    user.rating += ratingPoint
                elif KT_number == 2:
                    for lab_kt2 in labs_kt2:
                        if lab_kt2 == stats.lab:
                            ratingPoint = (lab_kt2.weight / 100) * kt[0].weight
                            if stats.status == True:
                                stats.status = False
                                stats.save()
                                if user.rating_2KT > 0:
                                    user.rating_2KT -= lab_kt2.weight
                                    user.rating -= ratingPoint
                            else:
                                stats.status = True
                                stats.save()
                                if user.rating_2KT >= 0:
                                    user.rating_2KT += lab_kt2.weight
                                    user.rating += ratingPoint
                else:
                    for lab_kt3 in labs_kt3:
                        if lab_kt3 == stats.lab:
                            ratingPoint = (lab_kt3.weight / 100) * kt[0].weight
                            if stats.status == True:
                                stats.status = False
                                stats.save()
                                if user.rating_3KT > 0:
                                    user.rating_3KT -= lab_kt3.weight
                                    user.rating -= ratingPoint
                            else:
                                stats.status = True
                                stats.save()
                                if user.rating_3KT >= 0:
                                    user.rating_3KT += lab_kt3.weight
                                    user.rating += ratingPoint
            if user.rating < 0:
                user.rating = 0
            
            
 



        user.save()
        stats.save()

    return JsonResponse(
        {
            'status': stats.status,
            'user_id': user.id,
            'lab_id': request.GET['stats_id'],
            'kt_1': float('{:.2f}'.format(user.rating_1KT)),
            'kt_2': float('{:.2f}'.format(user.rating_2KT)),
            'kt_3': float('{:.2f}'.format(user.rating_3KT)),
            'rating': float('{:.2f}'.format(user.rating))
        })

def view_info(request):
    student = Student.objects.filter(user=request.user)
    files = File.objects.filter(student=student[0])
    print(files[0].student)
    url = "/media/GroupProject.py"
    context = {
        'url': url,
        'files': files
    }
    return render(request, template_name='botbi20i1/info.html', context=context)

"""
    Функция добавление лабы
"""
def lab_add_view(request):

    weightKt1 = 100
    weightKt2 = 100
    weightKt3 = 100
    labsKt1 = Laboratory.objects.filter(kt=1)
    labsKt2 = Laboratory.objects.filter(kt=2)
    labsKt3 = Laboratory.objects.filter(kt=3)

    for labKt1 in labsKt1:
        weightKt1 -= labKt1.weight

    for labKt2 in labsKt2:
        weightKt2 -= labKt2.weight

    for labKt3 in labsKt3:
        weightKt3 -= labKt3.weight


    if request.method == 'POST':

        form = LabForm(request.POST)
        if form.is_valid():

            form.save()

            students = Student.objects.filter(group_id=request.POST['group_id'])
            lab = Laboratory.objects.filter(name=request.POST['name'])


            for student in students:

                if not Stats.objects.filter(lab=lab[0], student=student):

                    stats = Stats(student=student,
                                  lab=lab[0],
                                  status=False)
                    stats.save()
            return redirect(request.GET['next'])

    else:
        form = LabForm()

    context = {
        'form': form,
        'weightKt1': weightKt1,
        'weightKt2': weightKt2,
        'weightKt3': weightKt3
    }
    return render(request, template_name='botbi20i1/labCreate_page.html', context=context)



def lab_pk(pk):
    #/lab/52/?next=/group/10/
    lab_pk = ''
    change_pk = pk[5:-7]
    for i in change_pk:
        if i.isdigit():
            lab_pk += i
    return lab_pk




"""
    Функция добавления файла с заданием студента
"""
def FileAddView(request):
    if request.method == 'POST':

        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            pk = request.GET['next']
            print(request.GET)
            print(type(pk[5]))
            lab_id = lab_pk(request.GET['next'])
            print(lab_id)
            student = Student.objects.filter(user=request.user)
            lab = Laboratory.objects.filter(pk=lab_id)
            file = form.save(commit=False)
            file.lab = lab[0]
            file.student = student[0]

            file.save()



            print(lab[0])
            return redirect(request.GET['next'])
    else:
        form = FileForm()

    context = {
        'form': form
    }
    return render(request, template_name='botbi20i1/add_file.html', context=context)


"""
    Функция изменения файла студентом
"""
def FileChangeView(request):
    if request.method == 'POST':

        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            lab_id = lab_pk(request.GET['next'])
            student = Student.objects.filter(user=request.user)
            lab = Laboratory.objects.filter(pk=lab_id)
            File.objects.get(student=student[0], lab=lab[0]).delete()
            file = form.save(commit=False)
            file.lab = lab[0]
            file.student = student[0]
            file.save()

            return redirect(request.GET['next'])
    else:
        form = FileForm()

    context = {
        'form': form
    }
    return render(request, template_name='botbi20i1/change_file.html', context=context)


"""
    Функция удаления файла студентом
"""

def FileDeleteView(request):
    lab_id = lab_pk(request.GET['next'])
    student = Student.objects.filter(user=request.user)
    lab = Laboratory.objects.filter(pk=lab_id)
    File.objects.get(student=student[0], lab=lab[0]).delete()
    return redirect(request.GET['next'])






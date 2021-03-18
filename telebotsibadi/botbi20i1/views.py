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
        'form': form
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
    Страница пользователя 
"""
def user(request):

    students = Student.objects.all()
    stats = Stats.objects.all()
    teachers = Teacher.objects.all()
    groups = Group.objects.all()
    
    context = {
        'stats': stats,
        'students': students,
        'teachers': teachers, 
        'groups': groups
    }
    return render(request, template_name='botbi20i1/user_page.html', context=context)


"""
    Страница группы
"""
def group(request, group_id):
    students = Student.objects.filter(group_id__id=group_id)
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

"""
    Функция вывода главной страницы
"""
def facePage(request):
    students = Student.objects.all()
    groups = Group.objects.all()
    teachers = Teacher.objects.all()
    stats = Stats.objects.all().order_by('lab')

    context = {
        'groups': groups,
        'students': students,
        'teachers': teachers,
        'stats': stats,
    }

    return render(request, template_name='botbi20i1/face_page.html', context=context)


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
        print(kt[0].weight)
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
                            if stats.status == True:
                                stats.status = False
                                stats.save()
                                if user.rating_2KT > 0:
                                    user.rating_2KT -= lab_kt2.weight
                            else:
                                stats.status = True
                                stats.save()
                                if user.rating_2KT >= 0:
                                    user.rating_2KT += lab_kt2.weight
                else:
                    for lab_kt3 in labs_kt3:
                        if lab_kt3 == stats.lab:
                            if stats.status == True:
                                stats.status = False
                                stats.save()
                                if user.rating_3KT > 0:
                                    user.rating_3KT -= lab_kt3.weight
                            else:
                                stats.status = True
                                stats.save()
                                if user.rating_3KT >= 0:
                                    user.rating_3KT += lab_kt3.weight
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




                    #N = int(request.POST['kt'])
                    #labs_ktN = student.labs.filter(kt=N)
                    #s = Stats.objects.filter(student=student,status=True)
                #
                    #sum_true_lab_kt1 = 0
                    #sum_true_lab_kt2 = 0
                    #sum_true_lab_kt3 = 0
                    #
                    #for st in s:
                    #    if st.lab.kt == 1:
                    #        sum_true_lab_kt1 += 1
#
                    #    elif st.lab.kt == 2:
                    #        sum_true_lab_kt2 += 1
                    #    else:
                    #        sum_true_lab_kt3 += 1
                    #print(sum_true_lab_kt1)    
#
                    #if N == 1:
                    #    student.rating_1KT = 0
                    #    point_kt1 = round(100 / len(labs_ktN), 1)
                    #    student.rating_1KT = point_kt1 * sum_true_lab_kt1
                    #    
                    #elif N == 2:
                    #    student.rating_2KT = 0
                    #    point_kt2 = round(100 / len(labs_ktN), 1)
                    #    student.rating_2KT = point_kt2 * sum_true_lab_kt2
                    #else:
                    #    student.rating_3KT = 0
                    #    point_kt3 = round(100 / len(labs_ktN), 1)    
                    #    student.rating_3KT = point_kt3 * sum_true_lab_kt3
                    #
                    #print(student.name + " " + str(student.rating_1KT))
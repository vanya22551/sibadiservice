from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from .models import Student, Hint, Stats, Group, Laboratory, File, Teacher
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


def lab_add_view(request):
    if request.method == 'POST':
        print(type(request.POST['name']))
        form = LabForm(request.POST)
        if form.is_valid():

            form.save()
            students = Student.objects.filter(group_id=request.POST['group_id'])
            lab = Laboratory.objects.filter(name=request.POST['name'])
            
            for student in students:
                print(not Stats.objects.filter(lab=lab[0], student=student))
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


def FileChangeView(request):
    if request.method == 'POST':

        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            lab_id = lab_pk(request.GET['next'])
            student = Student.objects.filter(user=request.user)
            lab = Laboratory.objects.filter(pk=lab_id)
            f = File.objects.get(student=student[0], lab=lab[0]).delete()
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


def FileDeleteView(request):
    lab_id = lab_pk(request.GET['next'])
    student = Student.objects.filter(user=request.user)
    lab = Laboratory.objects.filter(pk=lab_id)
    file = File.objects.get(student=student[0], lab=lab[0]).delete()
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
            

#def EditTeacherInformationView(request):
#    if request.method == 'POST':
#        fm = EditTeacherInformationForm(request.POST)
#        if fm.is_valid():



def user(request):

    students = Student.objects.all()

    teachers = Teacher.objects.all()
    
    context = {
        'students': students,
        'teachers': teachers

    }
    return render(request, template_name='botbi20i1/user_page.html', context=context)


def group(request, group_id):
    students = Student.objects.filter(group_id__id=group_id)
    stats = Stats.objects.all().order_by('lab')
    teachers = Teacher.objects.all()
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

        'students': students,
        'studnt': studnt,

        'stats': stats,
    }

    return render(request, template_name='botbi20i1/group_page.html', context=context)


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


def studentPage(request, id):

    student = Student.objects.filter(user_id=id)
    stats = Stats.objects.filter(student=student[0])
    files = File.objects.filter(student=student[0])
    for file in files:
        print(file.lab.name)
    
    #for stat in stats:
     #   print(stat.lab.name)

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


def update_changes(request):
    if request.GET:
        stats = Stats.objects.get(pk=request.GET['stats_id'])
        user = Student.objects.get(pk=stats.student.id)
        labs_kt1 = user.labs.filter(kt=1)
        labs_kt2 = user.labs.filter(kt=2)
        labs_kt3 = user.labs.filter(kt=3)
        KT = stats.lab.kt

        sum_labs_1kt = len(labs_kt1)
        sum_labs_2kt = len(labs_kt2)
        sum_labs_3kt = len(labs_kt3)

        try:
            lab_point_kt1 = round(100 / sum_labs_1kt, 1)

        except ZeroDivisionError:
            lab_point_kt1 = 0

        try:
            lab_point_kt2 = round(100 / sum_labs_2kt, 1)

        except ZeroDivisionError:
            lab_point_kt2 = 0

        try:
            lab_point_kt3 = round(100 / sum_labs_3kt, 1)

        except ZeroDivisionError:
            lab_point_kt3 = 0

        if request.GET['status'] == '1':

            if user.rating_1KT <= 100 and user.rating_2KT <= 100 and user.rating_3KT <= 100:
                if KT == 1:
                    if stats.status == False:
                        stats.status = True
                        stats.save()
                        if user.rating_1KT >= 0:
                            user.rating_1KT += lab_point_kt1
                            if round(user.rating_1KT, 1) == 99.9:
                                user.rating_1KT += 0.1
                            elif round(user.rating_1KT, 1) == 100.1:
                                user.rating_1KT -= 0.1

                    else:
                        stats.status = False
                        stats.save()

                        if user.rating_1KT > 0:
                            user.rating_1KT -= lab_point_kt1
                            if round(user.rating_1KT, 1) == 0.1:
                                user.rating_1KT -= 0.1

                elif KT == 2:
                    if stats.status == False:
                        stats.status = True
                        stats.save()
                        if 100 > user.rating_2KT >= 0:
                            user.rating_2KT += lab_point_kt2
                            if round(user.rating_2KT, 1) == 99.9:
                                user.rating_2KT += 0.1
                            elif round(user.rating_2KT, 1) == 100.1:
                                user.rating_2KT -= 0.1

                    else:
                        stats.status = False
                        stats.save()
                        if 100 >= user.rating_2KT > 0:
                            user.rating_2KT -= lab_point_kt2
                            if round(user.rating_2KT, 1) == 0.1:
                                user.rating_2KT -= 0.1

                else:
                    if stats.status == False:
                        stats.status = True
                        stats.save()
                        if 100 >= user.rating_3KT >= 0:
                            user.rating_3KT += lab_point_kt3
                            if round(user.rating_3KT, 1) == 99.9:
                                user.rating_3KT += 0.1
                            elif round(user.rating_3KT, 1) == 100.1:
                                user.rating_3KT -= 0.1

                    elif stats.status == True:
                        stats.status = False
                        stats.save()
                        if 100 >= user.rating_3KT > 0:
                            user.rating_3KT -= lab_point_kt3
                            if round(user.rating_3KT, 1) == 0.1:
                                user.rating_3KT -= 0.1

        labs_done_kt1 = Stats.objects.filter(student=user, status=True, lab__kt=1)
        labs_done_kt2 = Stats.objects.filter(student=user, status=True, lab__kt=2)
        labs_done_kt3 = Stats.objects.filter(student=user, status=True, lab__kt=3)
        print(len(labs_kt1), len(labs_done_kt1))
        print(len(labs_kt2), len(labs_done_kt2))
        print(len(labs_kt3), len(labs_done_kt3))
        if len(labs_kt1) > 0 \
                and len(labs_kt2) > 0 \
                and len(labs_kt3) > 0:
            if len(labs_kt1) == len(labs_done_kt1) \
                    and len(labs_kt2) == len(labs_done_kt2) \
                    and len(labs_kt3) == len(labs_done_kt3):
                user.rating = 100
            else:
                user.rating = 0

        user.rating_1KT = round(user.rating_1KT, 2)
        user.rating_2KT = round(user.rating_2KT, 2)
        user.rating_3KT = round(user.rating_3KT, 2)
        user.rating = round(user.rating, 2)

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

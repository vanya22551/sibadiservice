from django.contrib.auth.models import User
from django.forms import ModelForm, HiddenInput, ModelChoiceField
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .models import Laboratory, Student, File, Teacher


class LabForm(ModelForm):
    class Meta:
        model = Laboratory
        fields = '__all__'


class FileForm(ModelForm):


    class Meta:
        model = File
        fields = {'file', 'lab', 'student'}




class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = {'password', 'username'}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'


class ChangePasswordForm(PasswordChangeForm, ModelForm):
    class Meta:
        model = User
        fields = {'old_password', 'new_password1', 'new_password2'}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'



class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = {'username', 'password'}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class EditTeacherInformationForm(ModelForm):
    class Meta:
        model = Teacher
        fields = {'email', 'phone', 'additional_information', }




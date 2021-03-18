from django.contrib import admin

# Register your models here.
from .models import Student, Laboratory, Hint, Stats, Group, File, Teacher, EducationControl

admin.site.register(Hint)
admin.site.register(Student)
admin.site.register(Laboratory)
admin.site.register(Stats)
admin.site.register(Group)
admin.site.register(File)
admin.site.register(Teacher)
admin.site.register(EducationControl)

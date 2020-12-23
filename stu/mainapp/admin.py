from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    pass


@admin.register(S_class)
class S_classAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass


@admin.register(T_C)
class T_CAdmin(admin.ModelAdmin):
    pass


@admin.register(S_C)
class S_CAdmin(admin.ModelAdmin):
    pass

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
STATE = (
    ('0', '老师'),
    ('1', '学生'),
    ('2', '管理员')
)


class CustomUser(AbstractUser):
    headpic = models.ImageField(verbose_name="头像", upload_to="user/headpic",
                                default='user/headpic/default.png')
    telephone = models.CharField(max_length=11, verbose_name="手机号码")
    state = models.CharField(max_length=1, default=1, choices=STATE, verbose_name='账号状态')


class Department(models.Model):
    d_name = models.CharField(max_length=20, verbose_name='院系名')
    d_id = models.CharField(max_length=11, verbose_name='院系序号')

    def __str__(self):
        return self.d_name


class Major(models.Model):
    m_name = models.CharField(max_length=11, verbose_name='专业名')
    m_id = models.CharField(max_length=11, verbose_name='专业编号')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='majors',
                                   verbose_name='所属院系')

    def __str__(self):
        return self.m_name


class S_class(models.Model):
    c_name = models.CharField(max_length=11, verbose_name='班级名')
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name='s_classes',
                              verbose_name='所属专业')

    def __str__(self):
        return self.c_name


class Student(models.Model):
    s_id = models.CharField(max_length=11, verbose_name='学号')
    name = models.CharField(max_length=11, verbose_name='姓名')
    age = models.CharField(max_length=3, verbose_name='性别')
    s_class = models.ForeignKey(S_class, on_delete=models.CASCADE, related_name='students',
                                verbose_name='所属班级')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    t_id = models.CharField(max_length=11, verbose_name='学号')
    name = models.CharField(max_length=11, verbose_name='姓名')
    age = models.CharField(max_length=3, verbose_name='性别')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers',
                                   verbose_name='所属院系')

    def __str__(self):
        return self.name


class Course(models.Model):
    co_name = models.CharField(max_length=11, verbose_name='课程名')
    credit = models.CharField(max_length=1, verbose_name='学分')

    def __str__(self):
        return self.co_name


class Score(models.Model):
    score = models.CharField(max_length=3, verbose_name='成绩')
    course = models.ForeignKey(Course, related_name='c_scores', verbose_name='所属课程',
                               on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='s_scores', verbose_name='所属学生',
                                on_delete=models.CASCADE)


class T_C(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='tcs', verbose_name='相关老师',
                                on_delete=models.CASCADE)
    course = models.ForeignKey(Teacher, related_name='cts', verbose_name='相关课程',
                               on_delete=models.CASCADE)


class S_C(models.Model):
    student = models.ForeignKey(Student, related_name='s_cs', verbose_name='相关学生',
                                on_delete=models.CASCADE)
    course = models.ForeignKey(Teacher, related_name='c_ss', verbose_name='相关课程',
                               on_delete=models.CASCADE)

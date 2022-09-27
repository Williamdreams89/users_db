from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from base.managers import UserManager




class User(AbstractBaseUser, PermissionsMixin):
    class RoleChoices(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        STUDENT = 'STUDENT', 'student'
        LECTURER = 'LECTURER', 'Lecturer'

    base_role = RoleChoices.STUDENT
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    role= models.CharField(max_length=100, choices=RoleChoices.choices)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "department", "role"]


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        
        results = super().get_queryset(*args,**kwargs)
        student_model = results.filter(role = User.RoleChoices.STUDENT)
        return student_model
    

class Student(User):
    base_role = User.RoleChoices.STUDENT

    students = StudentManager()

    class Meta:
        proxy = True
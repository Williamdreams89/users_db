from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin




class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    role= models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "department"]



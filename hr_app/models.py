from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import  AbstractBaseUser

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    address = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]


class EmployeeDetails(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=20)
    emp_name = models.CharField(max_length=30)
    emp_salary = models.IntegerField()
    hr_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.emp_id} {self.emp_name} {self.emp_salary} {self.hr_id}"


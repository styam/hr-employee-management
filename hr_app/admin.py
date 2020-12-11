from django.contrib import admin

from .models import User, EmployeeDetails


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'address', 'city']


admin.site.register(User, UserAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_id', 'emp_name', 'emp_salary', 'hr_id']

admin.site.register(EmployeeDetails, EmployeeAdmin)
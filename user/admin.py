from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'first_name', 'last_name', 'role','phone', 'password1', 'password2')}
        ),
    )



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','role','phone']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group) 
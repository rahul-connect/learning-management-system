
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email','role','phone')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name', 'email','phone')

        widgets={
                   "username":forms.TextInput(attrs={'class':'form-control','disabled':'disabled'}),
                   "first_name":forms.TextInput(attrs={'placeholder':'Enter UserName...','class':'form-control','disabled':'disabled'}),
                   "last_name":forms.TextInput(attrs={'placeholder':'Enter UserName...','class':'form-control','disabled':'disabled'}),
                   "email":forms.EmailInput(attrs={'placeholder':'Enter UserName...','class':'form-control','disabled':'disabled'}),
                   "phone":forms.NumberInput(attrs={'placeholder':'Enter UserName...','class':'form-control','disabled':'disabled'}),
                }  



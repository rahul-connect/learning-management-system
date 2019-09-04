from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout as logged_out,login as auto_login,update_session_auth_hash
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import CustomUser


# Create your views here.
def home(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		return render(request,'index.html')
	

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user:
			auto_login(request,user)
			return HttpResponseRedirect(reverse('dashboard'))
		else:
			messages.error(request,'Invalid User Credentials !!')
			return render(request,'index.html')

def dashboard(request):
	return render(request,'profile/dashboard.html')


def logout(request):
	logged_out(request)
	return HttpResponseRedirect(reverse('home'))


@login_required(login_url='/')
def user_profile(request):
	if request.method == "POST":
		form = CustomUserChangeForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request,'Profile Details Updated Successfully !!')
			return redirect('user_profile')
	else:
		form = CustomUserChangeForm(instance=request.user)
		context = {
			'form':form,
		}
		return render(request,'profile/profile.html',context)


@login_required(login_url='/')
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST,user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			messages.success(request,'Password Changed Successfully !!')
			return redirect('user_profile')
		else:
			messages.error(request,form.errors)
			form = PasswordChangeForm(user=request.user)
			context = {'form':form}
			return render(request,'profile/password.html',context)
			
	else:
		form = PasswordChangeForm(user=request.user)
		context = {
		'form':form
		}
		return render(request,'profile/password.html',context)


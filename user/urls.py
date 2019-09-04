from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('login/',views.login,name='login'),
	path('dashboard/',views.dashboard,name='dashboard'),
	path('logout/',views.logout,name='logout'),
	path('profile/',views.user_profile,name='user_profile'),
	path('password/',views.change_password,name='change_password'),
]
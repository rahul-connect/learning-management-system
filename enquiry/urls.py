from django.urls import path
from . import views

urlpatterns = [
	path('city/',views.city,name='city'),
	path('center/',views.center,name='center'),
	path('course/',views.course,name='course'),
	path('batch/',views.batch,name='batch'),
	path('my_course/',views.my_course,name='my_course'),
]
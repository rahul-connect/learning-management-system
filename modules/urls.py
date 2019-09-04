from django.urls import path
from . import views

urlpatterns = [
	path('new/',views.module,name='module'),
	path('contents/<int:s_id>',views.view_section,name='view_section'),
	path('section/',views.insert_section,name='section'),
	path('content/',views.insert_content,name='content'),
	path('upload_pdf/',views.upload_pdf,name='upload_pdf'),
	path('assignments/',views.view_assignments,name='assignments'),
	path('students/',views.view_students,name='students'),
	path('student_details/<int:s_id>',views.student_detail,name='student_detail'),
	path('create_user/<int:u_id>',views.create_user,name='create_user')
]
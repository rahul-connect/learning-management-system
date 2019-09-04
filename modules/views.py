from django.shortcuts import render,redirect
from .forms import NewModule,NewSection,NewVideoContent,NewPdfContent
from .models import Module,Section,Content,Assignment,Pdf
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from user.models import CustomUser
from enquiry.models import Enquiry
from quiz.models import Module_Completed
from datetime import date
from django.core.mail import send_mail
from django.conf import settings
from random import randint

# Create your views here.


def module(request):
	form = NewModule(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request,'Module Created Successfully !!')
		return redirect('module')


	#fetch_course = Course.objects.all().order_by('-created_on')
	context = {
		'form':form,
	}
	return render(request,'admin/module.html',context)



def view_section(request,s_id):
	if request.method == 'POST':
		student = request.user.id
		section_id = request.POST['section']
		section_instance = Section.objects.get(id=section_id)
		student_instance = CustomUser.objects.get(id=student)
		redirect_page = request.POST['redirect_page']
		file = request.FILES.get('assignment')
		fs = FileSystemStorage()
		filename = fs.save(file.name, file)
		uploaded_file_url = fs.url(filename)
		insert = Assignment(file=uploaded_file_url,section=section_instance,student=student_instance)
		insert.save()
		messages.success(request,'Assignment Uploaded Successfully !!')
		return redirect(redirect_page)

	# Else :
	get_section = Section.objects.get(id=s_id)
	get_content = Content.objects.filter(section=get_section)
	get_pdf = Pdf.objects.filter(section=get_section)

	context = {
		'get_section':get_section,
		'videos':get_content,
		'pdfs':get_pdf
	}
	return render(request,'profile/content.html',context)



def insert_section(request):
	form = NewSection(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request,'Section Created Successfully !!')
		return redirect('section')


	context = {
		'form':form,
	}
	return render(request,'admin/section.html',context)

def insert_content(request):
	form = NewVideoContent(request.POST or None)
	upload_pdf = NewPdfContent()

	if form.is_valid():
		form.save()
		messages.success(request,'Video Content Created Successfully !!')
		return redirect('content')
	
	context = {
		'form':form,
		'upload_pdf':upload_pdf
	}
	return render(request,'admin/content.html',context)



def upload_pdf(request):
	upload_pdf = NewPdfContent(request.POST,request.FILES)
	if upload_pdf.is_valid():
		upload_pdf.save()
		messages.success(request,'PDF Content Created Successfully !!')
		return redirect('content')
	else:
		messages.error(request,'ERROR Uploading PDF')
		return redirect('content')



def view_assignments(request):
	get_assignments = Assignment.objects.all().order_by('-submitted_on')
	context = {
		'assignments':get_assignments
		}
	return render(request,'admin/assignments.html',context)



def view_students(request):
	fetch_students = CustomUser.objects.filter(role='3').order_by('-id')
	fetch_details = Enquiry.objects.filter(lms_id='1')
	context = {
		'students':fetch_students,
		'details':fetch_details
		}
	return render(request,'admin/students.html',context)

def student_detail(request,s_id):
	student = CustomUser.objects.get(id=s_id)
	detail = Enquiry.objects.get(lms_username=student.username)
	assignments = Assignment.objects.filter(student=student)
	quiz_solved = Module_Completed.objects.filter(student=student) 

	def calculate_age(born):
	    today = date.today()
	    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

	age = calculate_age(detail.date_of_birth)

	context = {
		'student':detail,
		'assignments':assignments,
		'quiz_solved':quiz_solved,
		'age':age,
	}
	return render(request,'admin/student_detail.html',context)



def create_user(request,u_id):
	student = Enquiry.objects.get(id=u_id)
	random_num = str(randint(100000, 999999))
	generate_id = student.first_name.lower() + random_num
	username = generate_id.replace(" ", "")
	password = CustomUser.objects.make_random_password(length=14)
	print(username)
	print(password)
	

	create_user = CustomUser.objects.create_user(username=username,email=student.email,password=password,role=1,phone=student.contact,first_name=student.first_name,last_name=student.last_name)
	create_user.is_staff = False
	create_user.save

	subject = 'Congratulation ! ID has been created for your Task Management System'
	message = 'Your Credentials to login to Golearn \n Username: '+username+'\nPassword: '+password+'\n\n You can Change the password later in the account section after logging in'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [student.email,]
	send_mail( subject, message, email_from, recipient_list )

	student.tms_id = 1
	student.save()

	messages.success(request,'TMS ID Successfully Created !!')
	return redirect('students')







from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import NewCity,NewCenter,NewCourse,NewBatch
from .models import City,Center,Course,Batch,Enquiry
from modules.models import Module,Section
from quiz.models import Module_Completed
# Create your views here.



def city(request):
	form = NewCity(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request,'City Added Successfully !!')
		#form = NewCity()
		return redirect('city')

	fetch_cities = City.objects.all().order_by('-created_on')
	context = {
		'form':form,
		'cities':fetch_cities
	}
	return render(request,'admin/city.html',context)



def center(request):
	form = NewCenter(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request,'Center Added Successfully !!')
		return redirect('center')

	fetch_centers = Center.objects.all().order_by('-created_on')
	context = {
		'form':form,
		'centers':fetch_centers
	}
	return render(request,'admin/center.html',context)


def course(request):
	form = NewCourse(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request,'Course Added Successfully !!')
		return redirect('course')

	fetch_course = Course.objects.all().order_by('-created_on')
	context = {
		'form':form,
		'courses':fetch_course
	}
	return render(request,'admin/course.html',context)


def batch(request):
	form = NewBatch(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request,'Batch Created Successfully !!')
		return redirect('batch')

	#fetch_course = Course.objects.all().order_by('-created_on')
	context = {
		'form':form,
	}
	return render(request,'admin/batch.html',context)





# STudent View Function --------------------------------------------------------------------




def my_course(request):
	student = request.user
	
	get_user = Enquiry.objects.get(lms_username=student.username)
	get_course = Course.objects.get(id=get_user.course.id)
	get_module = Module.objects.filter(course=get_course)
	get_section = Section.objects.filter(module__course=get_course)

	check_quiz = Module_Completed.objects.filter(student=request.user.id)


	for module in get_module:
		if check_quiz.count() > 0:
			for quiz in check_quiz:
				if quiz.module == module:
					module.quiz = 1;


	context = {
	 'course_name': get_user.course,
	 'modules':get_module,
	 'sections':get_section,
	 'check_quiz':check_quiz,
	}

	return render(request,'profile/my_course.html',context)




from django.shortcuts import render,redirect
from .models import Quiz,Student_Answer,Module_Completed
from modules import models
from user.models import CustomUser
from .forms import NewQuiz
from django.contrib import messages

# Create your views here.



def start_quiz(request,m_id):
	student = CustomUser.objects.get(id=request.user.id)
	get_module = models.Module.objects.get(id=m_id)

	count_section = models.Section.objects.filter(module=get_module).count()
	check_assignments = models.Assignment.objects.filter(student=student,section__module=get_module).count()

	# Check if all assignments has been submitted of that module or not
	if check_assignments >= count_section:
		print('You can Give test')

	else:
		messages.error(request,'Please Complete Assignments of all '+str(count_section)+' Sections in '+get_module.title+' to Start the Quiz !!')
		return redirect('my_course')
	



	total_question = Quiz.objects.filter(module=get_module).count()

	if request.method == 'POST':
		correct = 0
		wrong=0
		for key, values in request.POST.lists():
			#print(key, values)
			if key != 'csrfmiddlewaretoken':
				#print('Student :'+str(request.user))
				#print('Question id:'+key)
				#print('Answer:'+values[0])
				#print(get_module)
				check_quiz = Quiz.objects.get(id=key)
				if check_quiz.correct == values[0]:
					correct+=1
					is_correct=1
				else:
					wrong+=1
					is_correct=0

				insert = Student_Answer(quiz=check_quiz,student=student,answer=values[0],is_correct=is_correct)
				insert.save()

		module_completed = Module_Completed(module=get_module,student=student,total_question=total_question,correct=correct,wrong=wrong)
		module_completed.save()
		return redirect('quiz_result',module=get_module.id)

	#Else get request	
	#check if he has already written th quiz

	get_quiz = Quiz.objects.filter(module=get_module)
	context = {
		'questions':get_quiz
	}
	return render(request,'profile/quiz.html',context)



def result(request,module):
	get_result = Module_Completed.objects.get(module=module,student=request.user)
	get_quiz = Quiz.objects.filter(module=module)
	get_answers = Student_Answer.objects.filter(quiz__module=module,student=request.user)

	context = {
		'result':get_result,
		'get_quiz':get_quiz,
		'get_answers':get_answers
	}
	return render(request,'profile/view_result.html',context)


def insert_quiz(request):
	form = NewQuiz(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request,'Quiz Created Successfully !!')
		return redirect('insert_quiz')


	context = {
		'form':form,	
	}
	return render(request,'admin/quiz.html',context)



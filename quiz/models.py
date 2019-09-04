from django.db import models
from modules.models import Module
from datetime import datetime
from django.conf import settings
# Create your models here.




class Quiz(models.Model):
	question = models.CharField(max_length=500)
	optionA = models.CharField(max_length=200,blank=True,null=True)
	optionB = models.CharField(max_length=200,blank=True,null=True)
	optionC = models.CharField(max_length=200,blank=True,null=True)
	optionD = models.CharField(max_length=200,blank=True,null=True)
	ans_choices = [('0', 'A'),('1', 'B'),('2', 'C'),('3', 'D'),]
	correct = models.CharField(max_length=2,choices=ans_choices)
	module = models.ForeignKey(Module,on_delete=models.CASCADE)
	created_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.question



class Student_Answer(models.Model):
	quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
	student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,limit_choices_to={'role':'3'})
	answer = models.CharField(max_length=2,blank=True,null=True)
	is_correct = models.CharField(max_length=2) # 0 for incorrect 1 for correct
	created_on = models.DateTimeField(default=datetime.now)



class Module_Completed(models.Model):
	module = models.ForeignKey(Module,on_delete=models.CASCADE)
	student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,limit_choices_to={'role':'3'})
	total_question = models.CharField(max_length=3,blank=True,null=True)
	correct = models.CharField(max_length=2,blank=True,null=True)
	wrong = models.CharField(max_length=2,blank=True,null=True)
	date = models.DateTimeField(default=datetime.now)

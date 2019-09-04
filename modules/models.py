from django.db import models
from enquiry.models import Course
from datetime import datetime
from django.conf import settings
# Create your models here.




class Module(models.Model):
	title = models.CharField(max_length=200)
	course = models.ForeignKey(Course,on_delete=models.CASCADE)
	created_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.title




class Section(models.Model):
	name = models.CharField(max_length=200)
	module = models.ForeignKey(Module,on_delete=models.CASCADE)
	created_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.name


class Content(models.Model):
	title = models.CharField(max_length=200,blank=True,null=True)
	video = models.CharField(max_length=800,blank=True,null=True)
	section = models.ForeignKey(Section,on_delete=models.CASCADE)
	created_on = models.DateTimeField(default=datetime.now)

class Pdf(models.Model):
	title = models.CharField(max_length=200,blank=True,null=True)
	file = models.FileField(upload_to='')
	section = models.ForeignKey(Section,on_delete=models.CASCADE)
	created_on = models.DateTimeField(default=datetime.now)


class Assignment(models.Model):
	file = models.FileField(upload_to='')
	section = models.ForeignKey(Section,on_delete=models.CASCADE)
	student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,limit_choices_to={'role':'3'})
	submitted_on = models.DateTimeField(default=datetime.now)

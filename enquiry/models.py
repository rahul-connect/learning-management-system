from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.

class City(models.Model):
	name = models.CharField(max_length=100)
	created_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.name


class Center(models.Model):
	name = models.CharField(max_length=100)
	city = models.ForeignKey(City,on_delete=models.CASCADE)
	created_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.name


class Course(models.Model):
	title = models.CharField(max_length=50)
	created_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.title


class Batch(models.Model):
	title = models.CharField(max_length=100)
	trainer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,limit_choices_to={'role':'4'})
	start_date = models.DateField(blank=True,null=True)
	end_date = models.DateField(blank=True,null=True)
	course = models.ForeignKey(Course,on_delete=models.CASCADE)
	TYPES = [('0', 'Basic Training'),('1', 'On Job Training'),]
	course_type = models.CharField(max_length=2,choices=TYPES)
	center = models.ForeignKey(Center,on_delete=models.CASCADE)
	DAYS = [('0', 'Weekdays'),('1', 'Weekends'),]
	days = models.CharField(max_length=2,choices=DAYS,default='0')
	class_start = models.TimeField(blank=True)
	class_end = models.TimeField(blank=True)
	created_on = models.DateTimeField(default=datetime.now)
	status = models.CharField(max_length=2,default=0)


	def __str__(self):
		return self.title


class Enquiry(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	gender = models.CharField(max_length=1)
	date_of_birth = models.DateField(blank=True,null=True)
	qualification = models.CharField(max_length=100)
	address = models.TextField(blank=True,null=True)
	experience = models.CharField(max_length=2)
	contact = models.CharField(max_length=12)
	email = models.CharField(max_length=50)
	course = models.ForeignKey(Course,on_delete=models.CASCADE)
	course_type = models.CharField(max_length=2)
	expected_date = models.DateTimeField(blank=True,null=True)
	follow_up = models.TextField(blank=True,null=True)
	lead_sourse = models.CharField(max_length=100)
	lead_date = models.DateField(blank=True,null=True)
	counsellor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,limit_choices_to={'role':'2'})
	created_on = models.DateTimeField(default=datetime.now)
	status = models.CharField(max_length=2,default=0)
	course_fee = models.CharField(max_length=7,blank=True,null=True,default=0)
	batch = models.ForeignKey(Batch,on_delete=models.CASCADE,null=True,blank=True)
	lms_id = models.CharField(max_length=2,default=0)
	lms_username = models.CharField(max_length=50,blank=True,null=True)
	tms_id = models.CharField(max_length=2,default=0)

	def __str__(self):
		return self.first_name
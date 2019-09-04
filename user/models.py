from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	ROLES = [('3', 'Student'),('4', 'Trainer'),('1','Executive')]
	role = models.CharField(max_length=2,choices=ROLES,default='3')
	phone = models.CharField(max_length=10, blank=True)
	






from django.contrib import admin
from .models import Course,City,Center,Batch
# Register your models here.

admin.site.register(City)
admin.site.register(Center)
admin.site.register(Course)
admin.site.register(Batch)
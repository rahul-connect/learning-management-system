from django.contrib import admin
from .models import Quiz,Student_Answer,Module_Completed
# Register your models here.

admin.site.register(Quiz)
admin.site.register(Student_Answer)
admin.site.register(Module_Completed)
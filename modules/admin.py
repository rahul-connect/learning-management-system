from django.contrib import admin
from .models import Module,Section,Content,Assignment,Pdf
# Register your models here.


admin.site.register(Module)
admin.site.register(Section)
admin.site.register(Content)
admin.site.register(Assignment)
admin.site.register(Pdf)
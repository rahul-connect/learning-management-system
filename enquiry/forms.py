from .models import City,Center,Course,Batch
from django import forms

class NewCity(forms.ModelForm):
	class Meta:
		model = City
		fields = ('name',)
		widgets={
                   "name":forms.TextInput(attrs={'placeholder':'','name':'name','id':'','class':'form-control form-control-alternative','required':'required'}),
                }


class NewCenter(forms.ModelForm):
      class Meta:
            model = Center
            fields = ('name','city',)
            widgets={
                   "name":forms.TextInput(attrs={'placeholder':'','name':'name','id':'','class':'form-control form-control-alternative','required':'required'}),
                   "city":forms.Select(attrs={'class':'form-control'}),
                }

class NewCourse(forms.ModelForm):
      class Meta:
            model = Course
            fields = ('title',)
            widgets={
                   "title":forms.TextInput(attrs={'placeholder':'','name':'name','id':'','class':'form-control form-control-alternative','required':'required'}),
                }


class NewBatch(forms.ModelForm):
      class Meta:
            model = Batch
            fields = ('title','trainer','start_date','end_date','course','course_type','center','days','class_start','class_end')
            widgets={
                   "title":forms.TextInput(attrs={'placeholder':'','name':'','id':'','class':'form-control'}),
                   "trainer":forms.Select(attrs={'class':'form-control'}),
                   "start_date":forms.DateInput(attrs={'class':'form-control date_pick','type': 'date','id':'','autocomplete':'off'}),
                   "end_date":forms.DateInput(attrs={'class':'form-control date_pick','type': 'date','id':'','autocomplete':'off'}),
                   "course":forms.Select(attrs={'class':'form-control'}),
                   "course_type":forms.Select(attrs={'class':'form-control'}),
                   "center":forms.Select(attrs={'class':'form-control'}),
                   "days":forms.Select(attrs={'class':'form-control'}),
                   "class_start":forms.TimeInput(attrs={'class':'form-control time_pick','type': 'time','id':''}),
                   "class_end":forms.TimeInput(attrs={'class':'form-control time_pick','type': 'time','id':''}),
                }
from .models import Quiz
from django import forms



class NewQuiz(forms.ModelForm):
      class Meta:
            model = Quiz
            fields = ('question','optionA','optionB','optionC','optionD','correct','module')
            widgets={
                   "question":forms.TextInput(attrs={'placeholder':'','class':'form-control form-control-alternative','required':'required'}),
                   "optionA":forms.TextInput(attrs={'placeholder':'','class':'form-control form-control-alternative','required':'required'}),
                   "optionB":forms.TextInput(attrs={'placeholder':'','class':'form-control form-control-alternative','required':'required'}),
                   "optionC":forms.TextInput(attrs={'placeholder':'','class':'form-control form-control-alternative','required':'required'}),
                   "optionD":forms.TextInput(attrs={'placeholder':'','class':'form-control form-control-alternative','required':'required'}),
                   "correct":forms.Select(attrs={'class':'form-control'}),
                   "module":forms.Select(attrs={'class':'form-control'}),
                }
from .models import Module,Section,Content,Pdf
from django import forms


class NewModule(forms.ModelForm):
      class Meta:
            model = Module
            fields = ('title','course',)
            widgets={
                   "title":forms.TextInput(attrs={'placeholder':'','name':'name','id':'','class':'form-control form-control-alternative','required':'required'}),
                   "course":forms.Select(attrs={'class':'form-control'}),
                }


class NewSection(forms.ModelForm):
      class Meta:
            model = Section
            fields = ('name','module',)
            widgets={
                   "name":forms.TextInput(attrs={'placeholder':'','class':'form-control form-control-alternative','required':'required'}),
                   "module":forms.Select(attrs={'class':'form-control'}),
                }


class NewVideoContent(forms.ModelForm):
      class Meta:
            model = Content
            fields = ('title','video','section',)
            widgets={
                   "title":forms.TextInput(attrs={'placeholder':'','class':'form-control form-control-alternative','required':'required'}),
                   "video":forms.TextInput(attrs={'placeholder':'paste youtube video url...','class':'form-control form-control-alternative','required':'required'}),
                   "section":forms.Select(attrs={'class':'form-control'}),
                }


class NewPdfContent(forms.ModelForm):
      class Meta:
            model = Pdf
            fields = ('title','file','section',)
            widgets={
                  "title":forms.TextInput(attrs={'placeholder':'','class':'form-control form-control-alternative','required':'required'}),
                   "file":forms.FileInput(attrs={'placeholder':'','class':'form-control form-control-alternative','required':'required'}),
                   "section":forms.Select(attrs={'class':'form-control'}),
                }



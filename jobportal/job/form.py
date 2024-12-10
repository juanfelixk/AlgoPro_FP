from django import forms
from .models import Job

class CreateJobForm(forms.ModelForm): #inheritance from ModelForm class in forms module
    class Meta: #inner class which allows modifications to the default ModelForm class
        model = Job
        exclude = ('user', 'company') #exclude user and company field from Job class

class UpdateJobForm(forms.ModelForm):
    class Meta: 
        model = Job
        exclude = ('user', 'company') 
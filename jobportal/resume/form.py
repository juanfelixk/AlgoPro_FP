from django import forms
from .models import Resume

class UpdateResumeForm(forms.ModelForm): #inheritance from ModelForm class in forms module
    class Meta: #inner class which allows modifications to the default ModelForm class
        model = Resume
        exclude = ('user', ) #exclude user field from Resume class
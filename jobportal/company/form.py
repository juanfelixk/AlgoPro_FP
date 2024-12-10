from django import forms 
from .models import Company

class UpdateCompanyForm(forms.ModelForm): #inheritance from ModelForm class in forms module
    class Meta: #inner class which allows modifications to the default ModelForm class
        model = Company
        exclude = ('user', ) #exclude user field from Company class
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class RegistrationForm(UserCreationForm): #inheritance from UserCreationForm class
    email = forms.EmailField(required=True) #set email field to required
    class Meta:
        model = get_user_model() #return User
        fields = ['email', 'password1', 'password2'] #password2 is used for confirmation
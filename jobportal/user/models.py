from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): #inheritance from AbstractUser class
    email = models.EmailField(unique=True) #ensure that email for each user is unique
    is_recruiter = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    has_resume = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)
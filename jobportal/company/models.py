from django.db import models
from user.models import User

class Company(models.Model): #inheritance from Model class in models module
    user = models.OneToOneField(User, on_delete = models.CASCADE) 
    #creates one-to-one relationship between User and Company (1 company is unique to 1 user)
    #deleting a User object will delete the respective Company object 
    name = models.CharField(max_length = 100, null = True, blank = True)
    city = models.CharField(max_length = 100, null = True, blank = True)
    est_date = models.PositiveIntegerField(null = True, blank = True)

    def __str__(self): #dunder method
        return self.name
from django.db import models
from user.models import User

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE) #creates one-to-one relationship (1 user is only allowed to have 1 resume)
    first_name = models.CharField(max_length = 100, null = True, blank = True)
    last_name = models.CharField(max_length = 100, null = True, blank = True)
    location = models.CharField(max_length = 50, null = True, blank = True)
    job_title = models.CharField(max_length = 50, null = True, blank = True)
    upload_resume = models.FileField(upload_to = 'resume', null = True, blank = True) #creates field that allows file uploading and store it in resume folder

    def __str__(self): #dunder method
        return f'{self.first_name} {self.last_name}'
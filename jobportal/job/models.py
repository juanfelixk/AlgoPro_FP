from django.db import models
from user.models import User
from company.models import Company

class Industry(models.Model): #inheritance from Model class in models module
    name = models.CharField(max_length = 100)

    def __str__(self): #dunder method
        return self.name

class Job(models.Model):
    #defines a tuple containing the format (actual database value, human-readable value) 
    job_type_choices = (
        ('Remote', 'Remote'),
        ('Onsite', 'Onsite'),
        ('Hybrid', 'Hybrid')
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE) #creates many-to-one relationship between Job and User
    company = models.ForeignKey(Company, on_delete = models.CASCADE) #creates many-to-one relationship between Job and Company
    title = models.CharField(max_length = 100) #creates a field with max-length of 100 characters
    location = models.CharField(max_length = 100)
    salary = models.PositiveBigIntegerField(default = 5000000) #set default salary as 5,000,000
    requirements = models.TextField()
    is_available = models.BooleanField(default = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    industry = models.ForeignKey(Industry, on_delete = models.CASCADE, null = True, blank = True) #creates many-to-one relationship between Job and Industry
    job_type = models.CharField(max_length = 20, choices = job_type_choices, null = True, blank = True)

    def __str__(self):
        return self.title
    
class ApplyJob(models.Model):
    status_choices = [
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending')
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE) #creates many-to-one relationship between ApplyJob and User
    job = models.ForeignKey(Job, on_delete = models.CASCADE) #creates many-to-one relationship between ApplyJob and Job
    timestamp = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 50, choices = status_choices)
from django.db import models
from user.models import User
from company.models import Company

class Industry(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Job(models.Model):
    job_type_choices = (
        ('Remote', 'Remote'),
        ('Onsite', 'Onsite'),
        ('Hybrid', 'Hybrid')
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    salary = models.PositiveBigIntegerField(default = 5000000)
    requirements = models.TextField()
    is_available = models.BooleanField(default = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    industry = models.ForeignKey(Industry, on_delete = models.CASCADE, null = True, blank = True)
    job_type = models.CharField(max_length = 20, choices = job_type_choices, null = True, blank = True)

    def __str__(self):
        return self.title
    
class ApplyJob(models.Model):
    status_choices = [
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending')
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    job = models.ForeignKey(Job, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 50, choices = status_choices)
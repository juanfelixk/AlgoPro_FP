from django.urls import path
from . import views #"." means importing from the same directory

urlpatterns = [
    path('', views.home, name = 'home'),
    path('job-list/', views.job_list, name = 'job-list'),
    path('job-details/<int:pk>/', views.job_details, name = 'job-details')
]

#the name of the list should be exactly "urlpatterns" as django only search and recognizes this

#1st parameter: url
#2nd parameter: call the needed function from views.py
#3rd parameter: give a name to each path()
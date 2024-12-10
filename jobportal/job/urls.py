from django.urls import path
from . import views #"." means importing from the same directory

urlpatterns = [
    path('create-job/', views.create_job, name = 'create-job'),
    path('update-job/<int:pk>/', views.update_job, name ='update-job'),
    path('manage-jobs/', views.manage_jobs, name = 'manage-jobs'),
    path('apply-to-job/<int:pk>/', views.apply_to_job, name = 'apply-to-job'),
    path('all-applicant<int:pk>/', views.all_applicant, name = 'all-applicant'),
    path('applied-job/', views.applied_job, name = 'applied-job'),
]

#the name of the list should be exactly "urlpatterns" as django only search and recognizes this

#1st parameter: url
#2nd parameter: call the needed function from views.py
#3rd parameter: give a name to each path()
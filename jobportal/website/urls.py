from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('job-list/', views.job_list, name = 'job-list'),
    path('job-details/<int:pk>/', views.job_details, name = 'job-details')
]
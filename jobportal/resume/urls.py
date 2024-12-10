from django.urls import path
from . import views

urlpatterns = [
    path('update-resume/', views.update_resume, name = 'update-resume'),
    path('view-resume/', views.view_resume, name = 'view-resume')
]
from django.urls import path
from . import views

urlpatterns = [
    path('update-company/', views.update_company, name = 'update-company'),
    path('view-company/', views.view_company, name = 'view-company')
]
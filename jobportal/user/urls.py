from django.urls import path
from . import views #"." means importing from the same directory

urlpatterns = [
    path('register-employee/', views.register_employee, name = 'register-employee'),
    path('register-recruiter/', views.register_recruiter, name = 'register-recruiter'),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout')
]

#the name of the list should be exactly "urlpatterns" as django only search and recognizes this

#1st parameter: url
#2nd parameter: call the needed function from views.py
#3rd parameter: give a name to each path()
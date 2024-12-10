from django.urls import path
from . import views #"." means importing from the same directory

urlpatterns = [
    path('', views.dashboard, name = 'dashboard')
]

#the name of the list should be exactly "urlpatterns" as django only search and recognizes this

#1st parameter: url
#2nd parameter: call the needed function from views.py
#3rd parameter: give a name to each path()
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegistrationForm
from resume.models import Resume
from company.models import Company

# Employee Registration
def register_employee(request):
    if request.method == 'POST': #check whether form is submitted
        form = RegistrationForm(request.POST) #retrieve information
        if form.is_valid():
            new_employee = form.save(commit=False)
            new_employee.is_employee = True
            new_employee.username = new_employee.email
            new_employee.save() #update new_employee object
            Resume.objects.create(user = new_employee) #automatically creates a resume object for new employee
            messages.info(request, 'Your account has been successfully created.') #notify user
            return redirect('login') #redirect user to url path named "login"
        else:
            messages.warning(request, 'An error occured. Please try again later.')
            return redirect('register-employee') #redirect user to url path named "register-employee"
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'user/register-employee.html', context) #display the form when the user first enter the page
    
# Recruiter Registration
def register_recruiter(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_recruiter = form.save(commit=False)
            new_recruiter.is_recruiter = True
            new_recruiter.username = new_recruiter.email
            new_recruiter.save()
            Company.objects.create(user = new_recruiter)
            messages.info(request, 'Your account has been successfully created.')
            return redirect('login')
        else:
            print(form.errors)
            messages.warning(request, 'An error occured. Please try again later.')
            return redirect('register-recruiter')
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'user/register-recruiter.html', context)
    
# User Login 
def login_user(request):
    if request.method == 'POST': #check whether form is submitted
        email = request.POST.get('email') #retrieve email from request object
        password = request.POST.get('password') #retrieve password from request object
        user = authenticate(request, username = email, password = password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard') #redirect user to url path named "dashboard" if login is succesful
        else:
            messages.warning(request, 'An error occured. Please try again later.')
            return redirect('login') #redirect user to url path named "login" if login is unsuccesful
    else:
        return render(request, 'user/login.html') #display the form when the user first enter the page
    
# User Logout
def logout_user(request):
    logout(request) #logout user
    messages.info(request, 'You have succesfully logged out.')
    return redirect('login') #redirect user to url path named "login" if logout is succesful
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegistrationForm
from resume.models import Resume
from company.models import Company

# Employee Registration
def register_employee(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_employee = form.save(commit=False)
            new_employee.is_employee = True
            new_employee.username = new_employee.email
            new_employee.save()
            Resume.objects.create(user = new_employee)
            messages.info(request, 'Your account has been successfully created.')
            return redirect('login')
        else:
            print(form.errors)
            messages.warning(request, 'An error occured. Please try again later.')
            return redirect('register-employee')
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'user/register-employee.html', context)
    
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
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username = email, password = password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'An error occured. Please try again later.')
            return redirect('login')
    else:
        return render(request, 'user/login.html')
    
# User Logout
def logout_user(request):
    logout(request)
    messages.info(request, 'You have succesfully logged out.')
    return redirect('login')
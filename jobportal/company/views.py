from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from user.models import User
from .form import UpdateCompanyForm

# Update Company Details
def update_company(request):
    if request.user.is_recruiter: #check whether user is a recruiter 
        company = Company.objects.get(user = request.user) #retrieve company object of the authenticated user
        if request.method == 'POST': #check whether form is submitted
            form = UpdateCompanyForm(request.POST, instance = company) #retrieve information inputted by the user
            if form.is_valid():
                update = form.save(commit = False) #save if form is valid, commit=False allows modifications before saving
                user = User.objects.get(id = request.user.id)
                user.has_company = True
                update.save() 
                user.save() #updating user object
                messages.info(request, 'Your company details have been updated.') #notify the user
                return redirect('dashboard') #redirect user to the url path named "dashboard"
            else:
                messages.warning(request, 'An error occured. Please try again later.') 
        else:
            form = UpdateCompanyForm(instance = company)
            context = {'form': form}
            return render(request, 'company/update-company.html', context) #display the webpage when user first enter the page 
    else:
        messages.warning(request, 'Request denined to due permission error.')
        return redirect('dashboard') #redirect user to url path named "dashboard" if user is not a recruiter

# View Company Details
def view_company(request, pk):
    company = Company.objects.get(pk = pk) #retrieve company object with the associated primary key (which indentifies user uniquely)
    context = {'company': company}
    return render(request, 'company/view-company.html', context) #display the webpage when user first enter the page
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Resume
from user.models import User
from .form import UpdateResumeForm

# Update Resume Details
def update_resume(request):
    if request.user.is_employee: #check whether user is an employee
        resume = Resume.objects.get(user = request.user) #retrieve Resume object of the authenticated user
        if request.method == 'POST': #check whether form is submitted
            form = UpdateResumeForm(request.POST, request.FILES, instance = resume) #retrieve information and file inputted by the user
            if form.is_valid(): 
                update = form.save(commit = False) #save is form is valid, commit=False allows modifications before saving
                user = User.objects.get(pk = request.user.id)
                user.has_resume = True
                user.save() #updating user object
                update.save()
                messages.info(request, 'Your resume details have been updated.') #notify the user
                return redirect('dashboard') #redirect user to the url path named "dashboard"
            else:
                messages.warning(request, 'An error occured. Please try again later')
        else:
            form = UpdateResumeForm(instance = resume)
            context = {'form': form}
            return render(request, 'resume/update-resume.html', context) #display the webpage when user first enter the page      
    else:
        messages.warning(request, 'Request denined to due permission error.')
        return redirect('dashboard') #redirect user to url path named "dashboard" if user is not an employee
    
# View Resume Details
def view_resume(request, pk): 
    resume = Resume.objects.get(pk = pk) #retrieve resume object with the associated primary key (which indentifies user uniquely)
    context = {'resume': resume}
    return render(request, 'resume/view-resume.html', context) #display the webpage when user first enter the page
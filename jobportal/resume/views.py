from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Resume
from user.models import User
from .form import UpdateResumeForm

# Update Resume Details
def update_resume(request):
    if request.user.is_employee: 
        resume = Resume.objects.get(user = request.user)
        if request.method == 'POST':
            form = UpdateResumeForm(request.POST, request.FILES, instance = resume)
            if form.is_valid():
                update = form.save(commit = False)
                user = User.objects.get(pk = request.user.id)
                user.has_resume = True
                user.save()
                update.save()
                messages.info(request, 'Your resume details have been updated.')
                return redirect('dashboard')
            else:
                print(form.errors)
                messages.warning(request, 'An error occured. Please try again later')
        else:
            form = UpdateResumeForm(instance = resume)
        context = {'form': form}
        return render(request, 'resume/update-resume.html', context)      
    else:
        messages.warning(request, 'Request denined to due permission error.')
        return redirect('dashboard')
    
def view_resume(request, pk):
    resume = Resume.objects.get(pk = pk)
    context = {'resume': resume}
    return render(request, 'resume/view-resume.html', context)
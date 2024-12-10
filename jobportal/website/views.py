from django.shortcuts import render, redirect
from job.models import Job, ApplyJob
from django.contrib import messages
from .filter import JobFilter

# Homepage
def home(request):
    return render(request, 'website/home.html') #display the homepage when the path is empty

# List of Jobs
def job_list(request):
    filter = JobFilter(request.GET, queryset = Job.objects.filter(is_available = True).order_by('-timestamp')) #filter job and order by latest
    context = {'filter': filter}
    return render(request, 'website/job-list.html', context) #display job-list.html to the user

# Job Details
def job_details(request, pk):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please log in to view job details and apply.') #do not allow user to view job details before logging in
        return redirect('job-list') #redirect user to the same page
    else:
        if ApplyJob.objects.filter(user = request.user, job = pk).exists(): #make sure the same user does not apply to the same job twice
            applied = True
        else:
            applied = False
        job = Job.objects.get(pk = pk)
        context = {'job': job, 'applied': applied}
        return render(request, 'website/job-details.html', context) #display job-details.html to user
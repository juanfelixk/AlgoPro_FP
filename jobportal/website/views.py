from django.shortcuts import render, redirect
from job.models import Job, ApplyJob
from django.contrib import messages
from .filter import JobFilter

def home(request):
    return render(request, 'website/home.html')

def job_list(request):
    filter = JobFilter(request.GET, queryset = Job.objects.filter(is_available = True).order_by('-timestamp'))
    context = {'filter': filter}
    return render(request, 'website/job-list.html', context)

def job_details(request, pk):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please log in to view job details and apply.')
        return redirect('job-list')
    else:
        if ApplyJob.objects.filter(user = request.user, job = pk).exists():
            applied = True
        else:
            applied = False
        job = Job.objects.get(pk = pk)
        context = {'job': job, 'applied': applied}
        return render(request, 'website/job-details.html', context)
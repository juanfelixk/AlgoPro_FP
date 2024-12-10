from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job, ApplyJob
from .form import CreateJobForm, UpdateJobForm

# Create Job
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateJobForm(request.POST)
            if form.is_valid():
                job = form.save(commit = False)
                job.user = request.user
                job.company = request.user.company
                job.save()
                messages.info(request, 'New job has been created.')
                return redirect('dashboard')
            else:
                messages.warning(request, 'An error occured. Please try again later.')
                return redirect('create-job')
        else:
            form = CreateJobForm()
            context = {'form': form}
            return render(request, 'job/create-job.html', context)
    else:
        messages.warning(request, 'Request denined to due permission error.')
        return redirect('dashboard')
    
# Update Job Info
def update_job(request, pk):
    job = Job.objects.get(pk = pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance = job)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your job details has been updated.')
            return redirect('manage-jobs')
        else:
            messages.warning(request, 'An error occured. Please try again later.')
    else:
        form = UpdateJobForm(instance = job)
        context = {'form': form}
        return render(request, 'job/update-job.html', context)

# Managing and Editing Posted Jobs
def manage_jobs(request):
    jobs = Job.objects.filter(user = request.user, company = request.user.company)
    context = {'jobs': jobs}
    return render(request, 'job/manage-jobs.html', context)

def apply_to_job(request, pk):
    if request.user.is_authenticated and request.user.is_employee:
        job = Job.objects.get(pk = pk)
        if ApplyJob.objects.filter(user = request.user, job = pk).exists():
            messages.warning(request, 'You have applied to this job.')
            return redirect('dashboard')
        else: 
            ApplyJob.objects.create(user = request.user, job = job, status = 'Pending')
            messages.info(request, 'You have successfully applied to this job.')
            return redirect('dashboard')
    else:
        messages.info(request, 'Please log in to continue.')
        return redirect('login')
    
def all_applicant(request, pk):
    job = Job.objects.get(pk = pk)
    applicants = job.applyjob_set.all()
    context = {'job': job, 'applicants': applicants}
    return render(request, 'job/all-applicant.html', context)

def applied_job(request):
    jobs = ApplyJob.objects.filter(user = request.user)
    context = {'jobs': jobs}
    return render(request, 'job/applied-job.html', context)
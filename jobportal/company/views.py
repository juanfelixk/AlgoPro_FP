from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from user.models import User
from .form import UpdateCompanyForm

# Update Company Details
def update_company(request):
    if request.user.is_recruiter:
        company = Company.objects.get(user = request.user)
        if request.method == 'POST':
            form = UpdateCompanyForm(request.POST, instance = company)
            if form.is_valid():
                update = form.save(commit = False)
                user = User.objects.get(id = request.user.id)
                user.has_company = True
                update.save()
                user.save()
                messages.info(request, 'Your company details have been updated.')
                return redirect('dashboard')
            else:
                messages.warning(request, 'An error occured. Please try again later.')
        else:
            form = UpdateCompanyForm(instance = company)
            context = {'form': form}
            return render(request, 'company/update-company.html', context)
    else:
        messages.warning(request, 'Request denined to due permission error.')
        return redirect('dashboard')

# View Company Details
def view_company(request, pk):
    company = Company.objects.get(pk = pk)
    context = {'company': company}
    return render(request, 'company/view-company.html', context)
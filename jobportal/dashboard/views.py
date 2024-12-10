from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

#returns an HTTPResponse containing the rendered HTML (provides user with the required webpage)
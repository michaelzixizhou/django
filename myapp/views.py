from django.shortcuts import render
from . import views
from django.http import HttpResponse
from .models import Project
# Create your views here.

def home_view(request, *args, **kwargs):
    context = {

    }
    return render(request, 'home.html', context)

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def portfolio_view(request, *args, **kwargs):
    print(request.user)
    projects = Project.objects.all()
    url = str(Project.image).replace('static', '')
    # sends information to templates
    context = { # Dict only has one entry fpr projects
        'project': projects, 'url': url
    }
    return render(request, 'portfolio.html', context)

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})
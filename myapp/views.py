from django.shortcuts import render
from . import views
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, 'home.html', {})
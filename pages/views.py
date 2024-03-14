from django.http import  HttpResponse
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_view(request):
    return  render(request, 'home/index.html', {})

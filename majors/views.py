from django.shortcuts import render, get_object_or_404 
from .models import Major
from classes.models import Class
# Create your views here.

def major(request, major_name):
    return render('major.html')
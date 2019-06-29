from django.shortcuts import render, redirect
from majors.models import *

def main(request):
    majors = Major.objects.all()

    return render(request, 'main.html', {'majors': majors})


def home(request):
    return redirect('main')
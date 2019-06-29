from django.shortcuts import render

# Create your views here.

def major(request):
    return render(request, 'major.html')
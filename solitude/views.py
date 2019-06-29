from django.shortcuts import render, redirect

def main(request):
    return render(request, 'main.html')


def home(request):
    return redirect('main')
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.
# 학과를 누르면 무슨 수업이 있는지 띄워주는 페이지
def main(request, major_id):
    classes = Class.objects.filter(major_id=major_id)

    return render(request, 'main.html', {'classes': classes})
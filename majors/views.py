from django.shortcuts import get_object_or_404, render
from .models import Major
from classes.models import *
# Create your views here.

# 학과를 누르면 수업 목록 보여주는 페이지
def main(request, id):
    classes = Class.objects.filter(major_id=id)

    return render(request, 'majors/main.html', {'classes': classes})
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from posts.models import *

# Create your views here.
# 수업을 누르면 게시판 띄워주기
def main(request, id):
    posts = Post.objects.filter(classname_id=id)

    return render(request, 'classes/main.html', {'posts': posts})

# 수업 게시판 개설 요청 페이지
def new(request):
    return render(request, 'classes/new.html')

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        major_id = request.POST.get('major_id')
        major = Major.objects.get(pk=major_id)
        
        new_class = Class(title=title, major=major)
        new_class.save()
    return redirect('majors:main', id=major_id)
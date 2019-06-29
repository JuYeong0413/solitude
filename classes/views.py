from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from posts.models import *

# Create your views here.
# 수업을 누르면 게시판 띄워주기
def main(request, id):
    posts = Post.objects.filter(classname_id=id)

    return render(request, 'classes/main.html', {'posts': posts})
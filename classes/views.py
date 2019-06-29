from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from posts.models import *

# Create your views here.
# 수업을 누르면 게시판 띄워주기
def main(request, id):
    user = request.user
    if user.is_anonymous:
        return render(request, 'account/login.html')
    else:
        posts = Post.objects.filter(classname_id=id)
        class_name = Class.objects.get(pk=id)

        return render(request, 'classes/main.html', {'posts': posts, 'class_name': class_name})

# 수업 게시판 개설 요청 페이지
def new_class(request):
    if request.method == "POST":
        major_id = request.POST.get('major_id')
    return render(request, 'classes/new_class.html', {'major_id': major_id})

def create_class(request):
    if request.method == "POST":
        title = request.POST.get('title')
        major_id = request.POST.get('major_id')
        major = Major.objects.get(pk=major_id)
        
        new_class = Class(title=title, major=major)
        new_class.save()
    return redirect('majors:main', id=major_id)



def new(request):
    return render(request, 'classes/new.html')


# 게시글 작성
def create(request):
    if request.method == 'POST':
        user = request.user
        category = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post(user=user, category=category, title=title, content=content)
        post.save()
        
        return redirect('show')


# 게시글 수정 페이지 띄우기
def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'classes/edit.html', {'post': post})


# 게시글 수정
def update(request, id):
    if request.method == 'POST':
        post = Post.objects.get(pk=id)
        category = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.category = category
        post.title = title
        post.content = content
        post.save()

        return redirect('home')


# 게시글 삭제
def delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('show')


# 댓글 작성
def create_comment(request, id):
    if request.method == 'POST':
        user = request.user
        post = Post.objects.get(pk=id)
        message = request.POST.get('message')

        comment = Comment(user=user, post=post, message=message)
        comment.save()

        return redirect('home')


# 댓글 삭제
def delete_comment(request, id):
    comment = Comment.objects.get(pk=id)
    comment.delete()

    return redirect('home')


# 좋아요
def like_toggle(request, id):
    user = request.user
    post = Post.objects.get(pk=id)
    
    is_like = user in post.likes.all()

    if is_like:
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return redirect('home')


# 게시글 목록보기
def list(request):
    user = request.user
    if user.is_anonymous:
        return render(request, 'account/login.html')
    else:
        posts = Post.objects.all()
        return render(request, 'classes/list.html', {'posts': posts})


# 게시글 검색
def search(request):
    if request.method == "POST":
        search = request.POST.get('search')
        posts = Post.objects.filter(title__contains=search)
    return render(request, 'classes/search.html', {'posts': posts})


def show(request, id):
    post = get_object_or_404(Post, pk=id)
    default_view_count = post.view_count
    post.view_count = default_view_count + 1
    post.save()
    return render(request, 'classes/show.html', {'post': post})
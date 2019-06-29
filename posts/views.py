from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User

# Create your views here.
# 게시글 작성 페이지 띄우기
def new(request):
    return render(request, 'posts/new.html')


# 게시글 작성
def create(request):
    if request.method == 'POST':
        user = request.user
        content = request.POST.get('content')
        image = request.FILES.get('file')

        post = Post(user=user, content=content, image=image)
        post.save()
        
        return redirect('home')


# 게시글 수정 페이지 띄우기
def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/edit.html', {'post': post})


# 게시글 수정
def update(request, id):
    if request.method == 'POST':
        post = Post.objects.get(pk=id)
        if request.FILES.get('file'):
            image = request.FILES['file']
            post.image = image
        content = request.POST.get('content')
        post.content = content
        post.save()

        return redirect('home')


# 게시글 삭제
def delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')


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


# 게시글 상세보기
def show(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/show.html', {'post': post})
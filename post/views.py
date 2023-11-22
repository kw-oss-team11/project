# post/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.http import JsonResponse

@login_required(login_url='/accounts/login/')
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

@login_required(login_url='/accounts/login/')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required(login_url='/accounts/login/')
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

@login_required(login_url='/accounts/login/')
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.username == post.author:
        post.delete()
    return redirect('post_list')

def increase_likes(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # 좋아요 숫자 증가
    post.likes += 1
    post.save()

    return JsonResponse({'likes': post.likes})

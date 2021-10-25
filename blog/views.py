from django.http.response import Http404
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view

from blog.serializers import PostSerializer
from .models import Post
from .forms import CommentForm, PostForm, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post, 'id': post.id, 'title': post.title, 'published_date': post.published_date, 'author':post.author})

class PostDetail(APIView):
    def get_object(self, title):
        try:
            return Post.objects.get(title=title)
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, title, format=None):
        post = self.get_object(title)
        serializer = PostSerializer(post)
        return Response(serializer.data)


@api_view(['GET'])
def all(request):
    posts = Post.objects.all().order_by('published_date')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_edit(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request, 'blog/post_edit.html',{'form':form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts':posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

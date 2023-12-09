from django.shortcuts import render
from .models import Post, User, Comment, Category

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def users(request):
    users_list = User.objects.all()
    return render(request, 'blog/users.html', {'users_list': users_list})

def blogs(request):
    blog_list = Post.objects.all()
    return render(request, 'blog/blogs.html', {'blog_list': blog_list})

def comments(request):
    comments_list = Comment.objects.all()
    return render(request, 'blog/comments.html', {'comments_list': comments_list})

def categories(request):
    categories_list = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories_list': categories_list})

def blog_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'blog/blogdetails.html', {'post': post, 'comments': comments})

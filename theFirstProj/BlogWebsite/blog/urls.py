from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/users', views.users, name='users'),
    path('blog/blogs/', views.blogs, name='blogs'),
    path('blog/comments/', views.comments, name='comments'),
    path('blog/categories/', views.categories, name='categories'),
    path('blog/<int:post_id>/', views.blog_details, name='blog_details'),
]
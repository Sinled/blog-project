from django.shortcuts import render
from blog_project.apps.blog.models import Blog


def blog_post(request):
    return render(request, "blog_post.html")


def blog(request):
    blog_post_list = Blog.objects.all()
    return render(request, "blog.html", {"blog_list": blog_post_list})

from django.shortcuts import render
from blog_project.apps.blog.models import Blog


def news(request):
    blog_post_list = Blog.objects.all()
    return render(request, "news.html", {"blog_list": blog_post_list})


def contacts(request):
    return render(request, "contacts.html")

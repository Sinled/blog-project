from django.http import HttpResponse
from django.views.generic.simple import direct_to_template


def news(request):
    return direct_to_template(request, "news.html")


def blog(request):
    return direct_to_template(request, "blog.html")


def contacts(request):
    return direct_to_template(request, "contacts.html")

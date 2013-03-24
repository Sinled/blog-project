from django.views.generic.simple import direct_to_template


def news(request):
    return direct_to_template(request, "news.html")


def contacts(request):
    return direct_to_template(request, "contacts.html")

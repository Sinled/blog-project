from django.contrib import admin
from blog_project.apps.blog.models import Blog
from blog_project.apps.blog.models import PostType

admin.site.register(Blog)
admin.site.register(PostType)

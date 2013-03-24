from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog_project.views.news', name='news'),
    url(r'^contacts/$', 'blog_project.views.contacts', name='contacts'),

    url(r'^blog/', include('blog_project.apps.blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

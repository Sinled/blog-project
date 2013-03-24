from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog_project.views.news', name='news'),
    url(r'^blog/$', 'blog_project.apps.blog.views.blog', name='blog'),
    url(r'^blog_post/(?P<post_id>\d+)/$', 'blog_project.apps.blog.views.blog_post', name='blog_post'),
    url(r'^contacts/$', 'blog_project.views.contacts', name='contacts'),
    # url(r'^blog_project/', include('blog_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

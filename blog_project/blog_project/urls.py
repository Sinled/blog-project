from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog_project.views.news', name='news'),
    url(r'^blog/$', 'blog_project.views.blog', name='blog'),
    url(r'^contacts/$', 'blog_project.views.contacts', name='contacts'),
    # url(r'^blog_project/', include('blog_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

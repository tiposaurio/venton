# _*_ coding: utf-8 _*_
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backengo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),





    url(r'^home/', include('apps.home.urls', namespace='home')),
    url(r'^$', 'apps.home.views.index', name='index'),

    url(r'^space/', include('apps.space.urls', namespace='space')),
    url(r'^sad/', include('apps.sad.urls', namespace='sad')),


    url(r'^mod_backend/',
        include('apps.mod_backend.urls', namespace='mod_backend')),
    url(r'^accounts/', include('apps.accounts.urls')),








    # http://stackoverflow.com/questions/19625102/django-javascript-translation-not-working
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),

    # https://docs.djangoproject.com/en/1.6/ref/views/
    # https://docs.djangoproject.com/en/1.6/howto/static-files/
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
        'show_indexes': settings.DEBUG
        }),
)


from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'plateo.views.home', name='home'),
    url(r'^saludo_hola/(?P<nombre>\w+)/$',
        'apps.home.views.saludo_hola_view', name='saludo-hola'),

    url(r'^saludo_hola_template/(?P<nombre>\w+)/$',
        'apps.home.views.saludo_hola_template_view',
        name='saludo-hola-template'),

    #url(r'^$', TemplateView.as_view(template_name='home/base_home.html')),

    url(r'^$', 'apps.home.views.index', name='index'),
    url(r'^index/$', 'apps.home.views.index', name='index'),


)

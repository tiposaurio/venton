from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from apps.mod_backend.views import dashboard

urlpatterns = patterns(
    '',

    # url(r'^dashboard/$', TemplateView.as_view(template_name="mod_backend/base_mod_backend.html"), name='dashboard'),
    url(r'^dashboard/$', dashboard, name='dashboard'),

)

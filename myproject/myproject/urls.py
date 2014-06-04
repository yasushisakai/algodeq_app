from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

                       ###################################
                       # basics
                       ###################################

                       url(r'^$', 'myproject.mainApp.views.index'),
                       #url(r'^$', TemplateView.as_view(template_name='index.html')),
                       url(r'^sign_up/', TemplateView.as_view(template_name='sign_up.html')),
                       url(r'^make/', TemplateView.as_view(template_name='make.html')),
                       url(r'^single/(?P<id>[-a-zA-Z0-9]+)/?$', TemplateView.as_view(template_name='single.html')),

                       # admin
                       url(r'^admin/',include(admin.site.urls)),

                       # media
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

                       ###################################
                       # unit testing
                       ###################################

                       ###################################
                       # batch operation
                       ###################################

                       url(r'^batch/', TemplateView.as_view(template_name='batch.html')),

                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
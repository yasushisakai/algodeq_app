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
                       url(r'^sign_up/', 'myproject.mainApp.views.sign_up'),
                       url(r'^signup/', 'myproject.mainApp.obsolete.views.register'),
                       url(r'^make/(?P<plan_id>[-0-9]+)/?$', 'myproject.mainApp.views.make'),
                       url(r'^plan/(?P<name>[-a-zA-Z0-9_]+)/?$', 'myproject.mainApp.views.single_plan'),

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


                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
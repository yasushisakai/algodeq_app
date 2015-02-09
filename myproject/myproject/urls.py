from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

                       # ##################################
                       # basics
                       ###################################

                       url(r'^$', 'myproject.mainApp.views.index'),  # 0.index tree diagram
                       url(r'^tree/', 'myproject.mainApp.views.tree'),  # tree diagram for submission
                       url(r'^make/(?P<plan_id>[-0-9]+)/?$', 'myproject.mainApp.views.make'),  # 1.create plan
                       url(r'^plan/(?P<name>[-a-zA-Z0-9_]+)/?$', 'myproject.mainApp.views.single_plan'),  # 2.view plan
                       url(r'finalize/', 'myproject.mainApp.views.finalize'),  # 3.save image and add plan to DB

                       url(r'^bot/(?P<type>[-0-9]+)/?$', 'myproject.mainApp.views.bot'),  # 4.fabrication
                       url(r'^bot_c/(?P<ids>[-0-9_]+)/?$', 'myproject.mainApp.views.controlled_bot'),
                       url(r'fabricate/', 'myproject.mainApp.views.fabricate'),

                       # authentication
                       url(r'log_out/', 'myproject.mainApp.views.log_out'),
                       url(r'^sign_up/', 'myproject.mainApp.views.sign_up'),

                       #information
                       url(r'^information/', 'myproject.mainApp.views.information'),
                       url(r'^archive/', 'myproject.mainApp.views.archive'),

                       #result
                       url(r'^result/', 'myproject.mainApp.views.result'),

                       # admin
                       url(r'^admin/', include(admin.site.urls)),

                       ###################################
                       # unit testing
                       ###################################

                       ###################################
                       # batch operation
                       ###################################


) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# use django serve if debug is true(local):
if settings.DEBUG:
    urlpatterns += patterns('', (
    r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
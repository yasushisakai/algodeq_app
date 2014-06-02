from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),

                       #index
                       # url(r'^$', 'myproject.mainApp.views.getRecursiveAll'),

                       #authentification
                       url(r'^$', 'myproject.mainApp.views.index'),
                       url(r'^logout/', 'myproject.mainApp.views.logout'),
                       url(r'^signup/', 'myproject.mainApp.views.register'),

                       #main
                       url(r'^main/', 'myproject.mainApp.views.getRecursiveAll'),

                       url(r'^obsolete/', 'myproject.mainApp.views.getPlansAll'),

                       #tree
                       url(r'^tree/', 'myproject.mainApp.views.getRecursiveAllTest'),

                       #single plans
                       url(r'^plan/(?P<id>[-a-zA-Z0-9]+)/?$', 'myproject.mainApp.views.getPlan'),

                       #single users
                       url(r'^user/(?P<id>[-0-9]+)/?$', 'myproject.mainApp.views.getUser'),

                       #ajax-test
                       url(r'^ajax/$', 'myproject.mainApp.views.ajax_test', name="ajax"),

                       #canvas-test
                       url(r'^canvas/$', 'myproject.mainApp.views.canvas_test'),

                       #sign-in
                       url(r'^sign-in/$', 'myproject.mainApp.views.canvas_test'),

                       #batch operations
                       url(r'^batch/', TemplateView.as_view(template_name='batch.html')),
                       url(r'^batch-addUser/', 'myproject.mainApp.views.batch_add_user'),
                       url(r'^batch-deleteUser/', 'myproject.mainApp.views.batch_delete_user'),
                       url(r'^batch-addPlan/', 'myproject.mainApp.views.batch_add_plan'),
                       url(r'^batch-deletePlan/', 'myproject.mainApp.views.batch_delete_plan'),

                       ##########################################################################################################
                       #testing
                       ('^diffTest/', TemplateView.as_view(template_name='diffTest.html')),
                       ('^saveImage/', 'myproject.mainApp.views.saveImage'),

                       ##########################################################################################################media and so on...
                       #media
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

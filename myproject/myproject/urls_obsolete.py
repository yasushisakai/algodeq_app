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
                       url(r'^$', 'myproject.mainApp.obsolete.views.index'),
                       url(r'^logout/', 'myproject.mainApp.obsolete.views.logout'),
                       url(r'^signup/', 'myproject.mainApp.obsolete.views.register'),

                       #main
                       url(r'^main/', 'myproject.mainApp.obsolete.views.getRecursiveAll'),

                       url(r'^obsolete/', 'myproject.mainApp.obsolete.views.getPlansAll'),

                       #tree
                       url(r'^tree/', 'myproject.mainApp.obsolete.views.getRecursiveAllTest'),

                       #single plans
                       url(r'^plan/(?P<id>[-a-zA-Z0-9]+)/?$', 'myproject.mainApp.obsolete.views.getPlan'),

                       #single users
                       url(r'^user/(?P<id>[-0-9]+)/?$', 'myproject.mainApp.obsolete.views.getUser'),

                       #ajax-test
                       url(r'^ajax/$', 'myproject.mainApp.obsolete.views.ajax_test', name="ajax"),

                       #canvas-test
                       url(r'^canvas/$', 'myproject.mainApp.obsolete.views.canvas_test'),

                       #sign-in
                       url(r'^sign-in/$', 'myproject.mainApp.obsolete.views.canvas_test'),

                       #batch operations
                       url(r'^batch/', TemplateView.as_view(template_name='obsolete/batch.html')),
                       url(r'^batch-addUser/', 'myproject.mainApp.obsolete.views.batch_add_user'),
                       url(r'^batch-deleteUser/', 'myproject.mainApp.obsolete.views.batch_delete_user'),
                       url(r'^batch-addPlan/', 'myproject.mainApp.obsolete.views.batch_add_plan'),
                       url(r'^batch-deletePlan/', 'myproject.mainApp.obsolete.views.batch_delete_plan'),

                       ##########################################################################################################
                       #testing
                       ('^diffTest/', TemplateView.as_view(template_name='obsolete/diffTest.html')),
                       ('^saveImage/', 'myproject.mainApp.obsolete.views.saveImage'),

                       ##########################################################################################################media and so on...
                       #media
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from myproject.veiws import hello

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ('^hello/$',hello),

    #index
    url(r'^$','myproject.mainApp.views.getRecursiveAll'),
    url(r'^obsolete/', 'myproject.mainApp.views.getPlansAll'),

    #tree
    url(r'^tree/','myproject.mainApp.views.getRecursiveAllTest'),

    #sign-in
    url(r'^signin/','myproject.mainApp.views.signin'),


    #single plans
    url(r'^plan/(?P<id>[-a-zA-Z0-9]+)/?$', 'myproject.mainApp.views.getPlan'),

    #single users
     url(r'^user/(?P<id>[-0-9]+)/?$', 'myproject.mainApp.views.getUser'),

    #ajax-test
    url(r'^ajax/$','myproject.views.ajax_test', name="ajax"),


    #batch operations
    url(r'^batch/', 'myproject.mainApp.views.batch'),
    url(r'^batch-addUser/', 'myproject.mainApp.views.batchAddUser'),
    url(r'^batch-deleteUser/', 'myproject.mainApp.views.batchDeleteUser'),
    url(r'^batch-addPlan/', 'myproject.mainApp.views.batchAddPlan'),
    url(r'^batch-deletePlan/', 'myproject.mainApp.views.batchDeletePlan'),

    ##########################################################################################################
    #testing
    ('^diffTest/','myproject.mainApp.views.diffTest'),
    ('^saveImage/','myproject.mainApp.views.saveImage'),


    ##########################################################################################################media and so on...
    #media
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    )+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

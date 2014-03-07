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
    url(r'^$','myproject.mainApp.views.getPlansAll'),

    #single plans
    url(r'^plan/(?P<name>[-a-zA-Z0-9]+)/?$', 'myproject.mainApp.views.getPlan'),

    #single users
     url(r'^user/(?P<name>[-a-zA-Z0-9]+)/?$', 'myproject.mainApp.views.getUser'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

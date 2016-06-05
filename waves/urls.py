from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^accounts/profile','wavesprofile.views.SeeProfile', name='profile1'),
    url(r'^profile/$','wavesprofile.views.SeeProfile', name='profile'),
    url(r'^events/$','events.views.Events', name='events'),
    url(r'^accommodation/$','accommodation.views.Accommodation', name='accommodation'),
    url(r'^profile/update/$','wavesprofile.views.FillProfile', name='fillprofile'),
    url(r'^print/passslip/$','print.views.PassSlip', name='printpass'),
    url(r'^barcode/$','print.views.barcode', name='barcode'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
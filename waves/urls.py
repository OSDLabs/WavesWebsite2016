from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile','wavesprofile.views.FillProfile', name='fillprofile'),
    url(r'^profile/','wavesprofile.views.SeeProfile', name='profile'),
]
#test

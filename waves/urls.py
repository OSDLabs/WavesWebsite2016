from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    url(r'^mobile/$', 'home.views.mobile', name='mobile'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile','wavesprofile.views.SeeProfile', name='profile1'),

    url(r'^profile/$','wavesprofile.views.SeeProfile', name='profile'),
    url(r'^dashboard/$','wavesprofile.views.Dashboard', name='dashboard'),
    url(r'^events/individual/$','events.views.Ind_Events', name='indevents'),
    url(r'^events/individual/([0-9]+)$','events.views.Ind_Events_Reg', name='indeventsreg'),
    url(r'^events/team/$','events.views.Team_Events', name='teamevents'),
    url(r'^events/team/([0-9]+)$','events.views.Team_Events_Reg', name='teameventsreg'),
    url(r'^events/teamcreate/([0-9]+)','team.views.Team_Create_Event', name='teamcreateevent'),

    url(r'^accommodation/$','accommodation.views.Accommodation', name='accommodation'),
    url(r'^profile/update/$','wavesprofile.views.FillProfile', name='fillprofile'),
    url(r'^print/passslip/$','print.views.PassSlip', name='printpass'),
    url(r'^barcode/$','print.views.barcode', name='barcode'),
    url(r'^api/profile/', include('wavesprofile.api.urls', namespace = "profile-api")),
    url(r'^api/events/', include('events.api.urls', namespace = "event-api")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^pronights/$', 'home.views.pronights', name='pronights'),
    url(r'^events/$', 'events.views.events', name='events'),
    url(r'^sponsors/$', 'sponsors.views.sponsors', name='sponsors'),
    url(r'^hospitality/$', 'home.views.hospitality', name='hospitality'),
    url(r'^previousyear/$', 'home.views.previousyear', name='previousyear'),
    url(r'^sightseeing/$', 'home.views.sightseeing', name='sightseeing'),
    url(r'^contact/$', 'home.views.contact', name='contact'),
    url(r'^team/$', 'home.views.team', name='team'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

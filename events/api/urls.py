from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
    # Examples:
    url(r'^$',EventListAPIView.as_view(), name='list'),

    ]
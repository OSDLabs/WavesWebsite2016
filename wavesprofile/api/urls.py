from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
    # Examples:
    url(r'^$',ProfileListAPIView.as_view(), name='list'),

    ]
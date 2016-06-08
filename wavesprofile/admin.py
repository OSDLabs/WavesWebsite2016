from django.contrib import admin
from .models import Profile,Institute,Department

admin.site.register([Profile,Institute,Department])
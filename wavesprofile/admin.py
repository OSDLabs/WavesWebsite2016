from django.contrib import admin
from .models import Profile,Institute,Department
# Register your models here.
admin.site.register([Profile,Institute,Department])
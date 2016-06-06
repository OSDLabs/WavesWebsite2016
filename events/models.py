from django.db import models

# Create your models here.
from wavesprofile.models import Profile

class Event(models.Model):
    eventName = models.CharField(max_length=100)
    user = models.ForeignKey(Profile,'user', null=True)
    eventDate = models.DateTimeField(null=True)

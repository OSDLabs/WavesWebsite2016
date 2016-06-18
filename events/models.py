from django.db import models

# Create your models here.
from wavesprofile.models import Profile
from django.contrib.auth.models import User

EVENT_TYPES = (
	(u'T',u'Team'),
	(u'S',u'Single'),
	)

CATEGORY = (
    (u'Drama',u'Drama'),
    (u'Dance',u'Dance'),
    (u'Big4',u'Big4'),
    (u'Business',u'Business'),
    (u'Fine Arts',u'Fine Arts'),
    (u'Literary',u'Literary'),
    (u'Music',u'Music'),
    (u'Film',u'Film'),
    (u'Photography',u'Photography'),
    (u'Quiz',u'Quiz'),
    (u'Special',u'Special'),
    )

class Event(models.Model):
    eventName = models.CharField(max_length=100)
    eventDate = models.DateTimeField(blank=True, null=True)
    eventRules = models.FileField(upload_to = "adminuploads/events/rules/" , blank=True, null=True)
    eventpic = models.ImageField(upload_to = "adminuploads/events/pics/" ,blank=True, null=True)
    event_desc = models.TextField(blank=True, null=True)
    event_type = models.CharField(max_length=1, choices=EVENT_TYPES)
    event_category = models.CharField(max_length=50, choices = CATEGORY, default='')

    def __str__(self):
        return self.eventName

class Indi_Event_Participants(models.Model):
	event = models.ForeignKey(Event, related_name = "event", on_delete = models.CASCADE)
	event_part = models.ForeignKey(User, related_name = "event_participating", on_delete = models.CASCADE)
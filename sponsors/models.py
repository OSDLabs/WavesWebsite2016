from django.db import models

from django.contrib.auth.models import User

# Create your models here.

CATEGORY = ((u'Title Sponsor', u'Title Sponsor'),
			(u'Media Partners', u'Media Partners'),
			(u'Event Partners', u'Event Partners'),
			(u'Food and Beverages Partners', u'Food and Beverages Partners'),
			(u'Ambience Partners', u'Ambiance Partners'),
			)


# CATEGORY = (u'Title Sponsor',
# 			u'Media Partners',
# 			u'Event Partners',
# 			u'Food and Beverages Partners',
# 			u'Ambiance Partners',
# 			)

class Sponsor(models.Model):
	sponsName = models.CharField(max_length=100)
	sponsPic = models.ImageField(upload_to = "adminuploads/sponsors/pics", blank=True, null=True)
	sponsCategory = models.CharField(max_length=50, choices=CATEGORY, default='')
	sponsURL = models.URLField(max_length=200, default="add sponsor's webpage")

	def __str__(self):
		return self.sponsName
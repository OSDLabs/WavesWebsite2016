from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
import registration
from image_cropping import ImageRatioField

GENDER_CHOICES = (
	(u'M',u'Male'),
	(u'F',u'Female'),
	(u'T',u'Transgender')
	)

YEAR_CHOICES = (
	(u'U1',u'Undergraduate 1st year'),
	(u'U2',u'Undergraduate 2nd year'),
	(u'U3',u'Undergraduate 3rd year'),
	(u'U4',u'Undergraduate 4th year'),
	(u'P1',u'Postgraduate 1st year'),
	(u'P2',u'Postgraduate 2nd year'),
	(u'SS',u'Schooling'),
	(u'PH',u'PhD.'),
	)


# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 120)
	# image = models.ImageField(upload_to = "uploads/profilepics/", default = '')
	# cropping = ImageRatioField('image', '430x430')
	email = models.EmailField()
	mobile = models.CharField(max_length = 10)
	institute = models.CharField(max_length = 120)
	department = models.CharField(max_length = 60)
	gender = models.CharField(max_length = 1, choices=GENDER_CHOICES)
	dob = models.DateField(auto_now_add = True, auto_now = False)
	year = models.CharField(max_length =2, choices = YEAR_CHOICES)
	updatedtime = models.DateTimeField(auto_now_add = False, auto_now = True)
	settime = models.DateTimeField(auto_now_add = True, auto_now = False)

class Institute(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name

class Department(models.Model):
	name= models.CharField(max_length=60)
	def __str__(self):
		return self.name


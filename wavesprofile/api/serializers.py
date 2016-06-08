from rest_framework.serializers import ModelSerializer
from wavesprofile.models import Profile

class ProfileSerializer(ModelSerializer):
	class Meta:
		model = Profile
		exclude = ['image']
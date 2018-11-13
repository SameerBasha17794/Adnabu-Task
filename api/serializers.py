from rest_framework import serializers
from .models import Adnabu



class AdnabuSerializer(serializers.ModelSerializer):
	url = serializers.URLField(write_only=True)
	class Meta:
		model = Adnabu
		fields = '__all__'
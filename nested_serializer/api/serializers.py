from api.models import Song, Singer
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = ['id', 'title', 'singer', 'duration']


class SingerSerializer(serializers.ModelSerializer):
	sung_by = SongSerializer(many=True, read_only=True)
	class Meta:
		model = Singer
		fields = ['id', 'name', 'gender', 'sung_by']
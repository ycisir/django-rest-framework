from api.models import Song, Singer
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
	singer = serializers.HyperlinkedIdentityField(view_name='singer-detail')
	class Meta:
		model = Song
		fields = ['id', 'title', 'singer', 'duration']


class SingerSerializer(serializers.ModelSerializer):
	# song = serializers.StringRelatedField(many=True, read_only=True) # userfull
	# song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail') # userfull
	# song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
	# song = serializers.HyperlinkedIdentityField(view_name='song-detail') # userfull


	class Meta:
		model = Singer
		fields = ['id', 'name', 'gender', 'song']
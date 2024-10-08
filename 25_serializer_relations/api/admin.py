from django.contrib import admin
from api.models import Singer, Song

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'gender']


@admin.register(Song)
class SingerAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'singer', 'duration']

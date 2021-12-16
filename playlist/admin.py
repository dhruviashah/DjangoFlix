from django.contrib import admin

from .models import Playlist,PlaylistItem
from videos.models import Video

class PlaylistItemInline(admin.TabularInline):
	model = PlaylistItem
	extra = 0

class PlaylistAdmin(admin.ModelAdmin):
	inlines = [PlaylistItemInline]
	class Meta:
		model = Playlist

# Register your models here.
admin.site.register(Playlist, PlaylistAdmin)

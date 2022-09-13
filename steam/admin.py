from django.contrib import admin
from .models import Channels

@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'key', 'has_output']
    list_display_links  = ['title']
    list_editable = ['has_output']
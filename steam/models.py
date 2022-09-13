import uuid
from django.db import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Channels(models.Model):
    title = models.CharField(max_length=255)
    key = models.UUIDField(default = uuid.uuid4, editable=False, unique=True)
    has_output = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(str(self.key), {'type': 'reload', 'output': str(self.has_output)})

        return super(Channels, self).save(*args, **kwargs)
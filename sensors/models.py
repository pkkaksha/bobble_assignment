from django.db import models
import datetime

# Create your models here.

class RoomTempData(models.Model):
    room_id = models.CharField(max_length=100)
    temp_in_room = models.IntegerField()
    changed_at = models.DateTimeField(default=datetime.datetime.now())


from rest_framework import serializers
from .models import RoomTempData


class RoomTempDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomTempData
        fields = ['room_id','temp_in_room']

class RoomTempDataFetchSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomTempData
        fields = ['room_id','temp_in_room',"changed_at"]
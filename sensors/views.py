from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from .serializers import RoomTempDataSerializer,RoomTempDataFetchSerializer
from .models import RoomTempData
from rest_framework import status


class TemperatureView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the  items
        '''
        room_temp = list(RoomTempData.objects.values())

        serializer = RoomTempDataFetchSerializer(room_temp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the temp for room
        '''
        data = {
            'room_id': request.data.get('room_id'),
            'temp_in_room': request.data.get('temp_in_room'),
        }
        serializer = RoomTempDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


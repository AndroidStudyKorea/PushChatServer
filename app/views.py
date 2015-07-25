# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import permissions, status, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app.models import Talk, Device
from app.serializers import DeviceSerializer, TalkSerializer


class DeviceView(GenericAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        if 'device_id' not in request.data or len(request.data['device_id']) < 5:
            return Response("device_id is required", status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = self.queryset.get(device_id=request.data['device_id'])
            request.data.pop('device_id')
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Device.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class TalkViewSet(viewsets.ModelViewSet):
    """
    채팅 메시지 엔드포인트
    """
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer
    permission_classes = (permissions.AllowAny,)

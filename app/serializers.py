# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from app.models import Device, Talk


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device


class TalkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talk

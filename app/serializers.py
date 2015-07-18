from rest_framework import serializers
from app.models import Talk


class TalkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Talk

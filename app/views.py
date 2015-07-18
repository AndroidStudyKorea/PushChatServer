from rest_framework import permissions
from rest_framework import viewsets
from app.models import Talk
from app.serializers import TalkSerializer


class TalkViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer
    permission_classes = (permissions.AllowAny,)

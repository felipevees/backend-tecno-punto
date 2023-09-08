from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from clients.models import Client
from clients.api.serializers import ClientSerializer


class ClientApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cc', 'asesor']

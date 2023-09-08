from rest_framework.serializers import ModelSerializer

from clients.models import Client
from users.api.serializers import UserSerializer


class ClientSerializer(ModelSerializer):
    asesor_data = UserSerializer(source='asesor', read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'cc',
                  'payment_value', 'payments', 'asesor', 'asesor_data']

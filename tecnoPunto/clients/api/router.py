from rest_framework.routers import DefaultRouter

from clients.api.views import ClientApiViewSet

router_client = DefaultRouter()

router_client.register(
    prefix='clients', basename='clients', viewset=ClientApiViewSet
)

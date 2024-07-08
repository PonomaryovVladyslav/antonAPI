from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from app.api.permissions import CreateOnlyByAdmin
from app.api.serializers import ItemSerializer, OrderWriteSerializer, OrderReadSerializer
from app.models import Item, Order


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ['get', 'post']
    permission_classes = [CreateOnlyByAdmin]
    authentication_classes = [TokenAuthentication]


class OrderViewSet(ModelViewSet):
    http_method_names = ['get', 'post']
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderWriteSerializer
        return OrderReadSerializer

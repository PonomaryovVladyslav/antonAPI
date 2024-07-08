from rest_framework.serializers import ModelSerializer

from app.models import Item, Order, OrderItem


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class OrderItemReadSerializer(ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = OrderItem
        fields = ["item", "quantity"]


class OrderItemWriteSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["item", "quantity"]


class OrderReadSerializer(ModelSerializer):
    items = OrderItemReadSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', "order_date", "items"]


class OrderWriteSerializer(ModelSerializer):
    items = OrderItemWriteSerializer(many=True, allow_null=False, allow_empty=False, write_only=True)

    class Meta:
        model = Order
        fields = ['id', "order_date", "items"]

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = super().create(validated_data)
        order_items = [OrderItem(order=order, **item) for item in items]
        OrderItem.objects.bulk_create(order_items)
        return order

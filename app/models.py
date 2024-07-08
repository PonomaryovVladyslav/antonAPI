# Create your models here.
from django.db import models

GOOD_TYPE = (
    ("Snack", "Snack"),
    ("Coffee", "Coffee")
)


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.CharField(max_length=100, choices=GOOD_TYPE)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

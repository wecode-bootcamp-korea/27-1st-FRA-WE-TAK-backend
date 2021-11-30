from django.db       import models
from products.models import Product
from users.models    import User


class Cart(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count   = models.IntegerField()

    class Meta:
        db_table = 'carts'

class Order(models.Model):
    order_number = models.IntegerField()
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.ForeignKey('Order', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'order_status'

class OrderItems(models.Model):
    order             = models.ForeignKey('Order', on_delete=models.CASCADE)
    count             = models.IntegerField()
    tracking_number   = models.CharField(max_length=200)
    product           = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_item_status = models.ForeignKey('Order_item_status', on_delete=models.CASCADE)

    class Meta:
        db_table = 'order_items'

class OrderItemStatus(models.Model):
    name = models.CharField(max_length=100)

from django.db import models
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password= models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='users'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Products_Category',on_delete=CASCADE)
    rating = models.IntegerField()
    image_description = models.URLField()
    create_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

    class Meta:
        db_table='products'

class Products_Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table='product_category'

class Image(models.Model):
    product = models.ForeignKey('Product',on_delete=CASCADE)
    image = models.URLField()

    class Meta:
        db_table='images'

class Review(models.Model):
    user = models.ForeignKey('User', on_delete=CASCADE)
    product = models.ForeignKey('Product', on_delete=CASCADE)
    content = models.TextField()

    class Meta:
        db_table='reviews'

class Cart(models.Model):
    user = models.ForeignKey('User',on_delete=CASCADE)
    product = models.ForeignKey('Product', on_delete=CASCADE)
    count = models.IntegerField()

    class Meta:
        db_table='carts'

class Order(models.Model):
    order_number = models.IntegerField()
    user = models.ForeignKey('User',on_delete=CASCADE)
    order_status = models.ForeignKey('',on_delete=CASCADE)

    class Meta:
        db_table='orders'

class Order_status(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table='order_status'

class Order_items(models.Model):
    order = models.ForeignKey('Order', on_delete=CASCADE)
    count = models.IntegerField()
    tracking_number = models.CharField(max_length=200)
    product = models.ForeignKey('Product',on_delete=CASCADE)
    order_item_status = models.ForeignKey('Order_item_status',on_delete=CASCADE)

    class Meta:
        db_table='order_items'

class Order_item_status(models.Model):
    name = models.CharField(max_length=100)
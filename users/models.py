from django.db       import models
from products.models import Product


class User(models.Model):
    name      = models.CharField(max_length=100)
    email     = models.CharField(max_length=100)
    password  = models.CharField(max_length=200)
    contact   = models.CharField(max_length=100)
    address   = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'users'

class Review(models.Model):
    user    = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        db_table = 'reviews'
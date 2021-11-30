from django.db import models


class Product(models.Model):
    name              = models.CharField(max_length=100)
    price             = models.DecimalField(max_digits=10, decimal_places=2)
    category          = models.ForeignKey('Category', on_delete=models.CASCADE)
    rating            = models.IntegerField()
    image_description = models.URLField()
    create_at         = models.DateTimeField(auto_now_add=True)
    update_at         = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image   = models.URLField()

    class Meta:
        db_table = 'images'
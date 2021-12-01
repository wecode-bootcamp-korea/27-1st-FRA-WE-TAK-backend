from django.db    import models
from users.models import User



class Product(models.Model):
    name               = models.CharField(max_length=100)
    price              = models.DecimalField(max_digits=10, decimal_places=2)
    sub_category       = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    rating             = models.IntegerField(null=True)
    image_description  = models.URLField()
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at         = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        
class MainCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'main_categories'

class SubCategory(models.Model):
    name          = models.CharField(max_length=100)
    main_category = models.ForeignKey('MainCategory', on_delete=models.CASCADE)

    class Meta:
        db_table = 'sub_categories'

class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image   = models.URLField()

    class Meta:
        db_table = 'images'

class Like(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'
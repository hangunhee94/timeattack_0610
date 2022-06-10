from email.headerregistry import Address
from django.db import models

# Create your models here.
class Product(models.Model):
    class Meta:
        db_table = "products"

    name = models.CharField(max_length=256)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image = models.CharField(max_length=256,default=True )
    description = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    stock = models.CharField(max_length=256)
    
class Category(models.Model):
    class Meta:
        db_table = "categories"

    name = models.CharField(max_length=256)

class OrderStatus(models.Model):
    class Meta:
        db_table = "orders"

    statusname = models.CharField(max_length=256)

class ProductOrder(models.Model):
    class Meta:
        db_table = "productorders"

    productsave = models.CharField(max_length=256)

class UserOrder(models.Model):
    class Meta:
        db_table = "userorders"
    
    address = models.CharField(max_length=256)
    ordertime = models.CharField(max_length=256)
    allprice = models.CharField(max_length=256)
    sale = models.CharField(max_length=256)
    finalprice = models.CharField(max_length=256)
    validity = models.CharField(max_length=256)
    
    




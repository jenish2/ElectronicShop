from django.db import models
from shop.models import Product

# Create your models here.
class Order(models.Model):
    user_id = models.CharField(max_length=20)
    o_date = models.DateField('date published')
    price = models.FloatField(max_length=10)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=1)
    images = models.CharField(max_length=30, default='')
    item = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.user_id

class Ordered(models.Model):
    user_id = models.CharField(max_length=20)
    o_date = models.DateField('date published')
    price = models.FloatField(max_length=10)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE,)
    quantity = models.IntegerField(default=1)
    images = models.CharField(max_length=30, default='')
    item = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.user_id
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product_id=models.AutoField
    product_number = models.CharField(default=None,max_length=20)
    product_name=models.CharField(default=None,null=False,max_length=100)
    catagory=models.CharField(default=None,max_length=50)
    product_discription=models.CharField(max_length=900)
    #stock=models.IntegerField(default=0)
    price=models.FloatField(default=0.0,null=False)
    img=models.ImageField(upload_to="eshop/images/", default="a.jpeg")

    def __str__(self):
        return self.product_name


class ContactUS(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70 ,default="")
    phone=models.CharField(max_length=70,default="")
    desc=models.CharField(max_length=70,default="")
    def __str__(self):
        return self.name
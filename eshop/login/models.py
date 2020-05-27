from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id=models.AutoField                    
    customer_name=models.CharField(max_length=20)
    password=models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    gender = models.CharField(max_length=6)
    mobile_no = models.BigIntegerField()
    address = models.CharField(max_length=200, default='')
    cimg=models.ImageField(upload_to="login/images/" ,default="p.jpg")

    def __str__(self):
        return self.customer_name

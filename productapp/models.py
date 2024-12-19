from django.db import models

# Create your models here.
class productprice(models.Model):
    customer_name = models.CharField(max_length=100)
    product1 = models.IntegerField()
    product2 = models.IntegerField()
    product3 = models.IntegerField()
    product4 = models.IntegerField()
    product5 = models.IntegerField()







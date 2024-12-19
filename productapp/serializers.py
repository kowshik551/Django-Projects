from rest_framework import serializers
from .models import productprice

class productpriceserializers(serializers.ModelSerializer):
    class Meta:
        model = productprice
        fields = ['id','customer_name','product1','product2','product3','product4','product5']

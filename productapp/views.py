from django.shortcuts import render
from .models import productprice
from .serializers import productpriceserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['POST'])
def products(request):
    if request.method == 'POST':
        serializer = productpriceserializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def products_id(request,id):
    products = productprice.objects.get(pk=id)

    if request.method == 'GET':
        serializer = productpriceserializers(products)
        print(serializer.data)

        total_bill = serializer.data['product1'] + serializer.data['product2'] + serializer.data['product3'] + serializer.data['product4'] + serializer.data['product4'] + serializer.data['product5']
        print(f'total_bill = {total_bill}')
        actual_bill = total_bill

        discount_10 = total_bill -100
        discount_20 = total_bill -400
        if (total_bill>000 and total_bill<2000):
              total_bill = discount_10
        elif (total_bill>2000):
              total_bill = discount_20
              final_bill = total_bill
              print(f'final_bill = {total_bill}')
        data = {}
        data['customer_name'] = serializer.data['customer_name']
        data['product1'] = serializer.data['product1']
        data['product2'] = serializer.data['product2']
        data['product3'] = serializer.data['product3']
        data['product4'] = serializer.data['product4']
        data['product5'] = serializer.data['product5']
        data['total_bill'] = actual_bill
        data['final_bill'] = final_bill
        return Response (data)


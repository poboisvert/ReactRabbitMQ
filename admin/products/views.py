# from django.shortcuts import render
# Create your views here.
import random

from .serializers import ProductSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product, User
from .serializers import ProductSerializer
from .producer import publish

from rest_framework.views import APIView

# Views
class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        # Rabbit MQ
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # DB action
        serializer.save()
        # RabbitMQ
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): # pk = primary key
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)

         # DB action
        product.delete()
        # RabbitMQ
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserCallView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
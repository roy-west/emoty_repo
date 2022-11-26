from rest_framework import viewsets
from .models import Shop, Category, Product
from .serializers import ShopSerializer, CategorySerializers, ProductSerializers


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product
    serializer_class = ProductSerializers



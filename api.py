from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
from .Serializer import ProductSerializer
from .models import Product


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    #permission_classes = [IsAuthenticated]
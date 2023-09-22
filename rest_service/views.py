from django.shortcuts import render
from .serializers import StoreModelSerializer
from .models import Store,Products
from rest_framework import viewsets

# Create your views here.

class StoreViewset(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreModelSerializer
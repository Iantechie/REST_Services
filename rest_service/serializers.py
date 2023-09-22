from .models import Store, Products
from rest_framework import serializers

class StoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        
class ProductsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
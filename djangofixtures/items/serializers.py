from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class meta:
        model = Item
        fiels = '__all__'
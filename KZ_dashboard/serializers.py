from rest_framework import serializers
from .models  import *

class ItemsSerializer(serializers.ModelSerializer):
    class Meta():
        model = KZ_dashboard
        fields = "__all__"
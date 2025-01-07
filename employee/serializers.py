from rest_framework import serializers
from .models import Hundred
from django.db.models import fields

class HundredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hundred
        fields = '__all__'
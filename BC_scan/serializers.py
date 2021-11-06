from django.db.models import fields
from rest_framework import serializers
from .models import BusinessCard, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'name', 'created_at', 
        )

class BusinessCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCard
        fields = (
            'name', 'mobile_tell', 'email', 
            'fax', 'company', 'company_address', 
            'company_tell', 'com_extension_tell', 'created_at', 
            )



from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = Account
        fields = ('type','displayName')
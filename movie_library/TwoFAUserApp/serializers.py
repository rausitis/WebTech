from rest_framework import serializers
from .models import TwoFAUser


class TwoFAUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwoFAUser
        fields = '__all__'

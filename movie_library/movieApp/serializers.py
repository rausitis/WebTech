from rest_framework import serializers
from .models import UserInfo
from .models import Content
from .models import CastMembers
from .models import FavoriteContent
from .models import MovieMakers


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['firstname', 'lastname', 'email', 'phoneNo', 'password']

    def create(self, validated_data):
        user = UserInfo (
            firstname = validated_data['firstname'],
            lastname = validated_data['lastname'],
            email = validated_data['email'],
            phoneNo = validated_data['phoneNo']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class CastMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastMembers
        fields = '__all__'


class FavoriteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteContent
        fields = '__all__'


class MovieMakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieMakers
        fields = '__all__'

from rest_framework import serializers
from django import forms
from .models import UserInfo
from .models import Content
from .models import CastMembers
from .models import FavoriteContent
from .models import MovieMakers
from .models import Code


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


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


class CodeForm(forms.Form):
    codenumber = forms.CharField(label='Code',
                                       help_text='Enter SMS verification code')

    class Meta:
        model = Code
        fields = ('codenumber',)

from rest_framework import status
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist


class UserInfoViewset(APIView):
    def get(self, request, id=None):
        if id:
            try:
                item = models.UserInfo.objects.get(id=id)
                serializer = serializers.UserInfoSerializer(item)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK
                )
            except models.UserInfo.DoesNotExist:
                return Response(
                    {"status": "error", "data": "User not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        items = models.UserInfo.objects.all()
        serializer = serializers.UserInfoSerializer(items, many=True)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def post(self, request, id=None):
        serializer = serializers.UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, id=None):
        try:
            item = models.UserInfo.objects.get(id=id)
            serializer = serializers.UserInfoSerializer(
                item, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"status": "error", "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except models.UserInfo.DoesNotExist:
            return Response(
                {"status": "error", "data": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, id=None):
        item = models.UserInfo.objects.all()
        print(item)
        item.delete()
        return Response(
            {"status": "success", "data": "Item Deleted"}
        )


class ContentViewset(APIView):
    def get(self, request, id=None):
        if id:
            try:
                item = models.Content.objects.get(id=id)
                serializer = serializers.ContentSerializer(item)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK
                )
            except models.Content.DoesNotExist:
                return Response(
                    {"status": "error", "data": "Content not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        items = models.Content.objects.all()
        serializer = serializers.ContentSerializer(items, many=True)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def post(self, request, id=None):
        serializer = serializers.ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, id=None):
        try:
            item = models.Content.objects.get(id=id)
            serializer = serializers.ContentSerializer(
                item, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"status": "error", "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except models.Content.DoesNotExist:
            return Response(
                {"status": "error", "data": "Content not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, id=None):
        item = models.Content.objects.filter(id=id)
        print(item)
        item.delete()
        return Response(
            {"status": "success", "data": "Item Deleted"}
        )


class CastMembersViewset(APIView):
    def get(self, request, id=None):
        if id:
            try:
                item = models.CastMembers.objects.get(id=id)
                serializer = serializers.CastMembersSerializer(item)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK
                )
            except models.CastMembers.DoesNotExist:
                return Response(
                    {"status": "error", "data": "CastMembers not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        items = models.CastMembers.objects.all()
        serializer = serializers.CastMembersSerializer(items, many=True)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def post(self, request, id=None):
        serializer = serializers.CastMembersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, id=None):
        try:
            item = models.CastMembers.objects.get(id=id)
            serializer = serializers.ContentSerializer(
                item, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"status": "error", "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except models.CastMembers.DoesNotExist:
            return Response(
                {"status": "error", "data": "CastMembers not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, id=None):
        item = models.CastMembers.objects.filter(id=id)
        print(item)
        item.delete()
        return Response(
            {"status": "success", "data": "Item Deleted"}
        )


class FavoriteContentViewset(APIView):
    def get(self, request, id=None):
        if id:
            try:
                item = models.FavoriteContent.objects.get(id=id)
                serializer = serializers.FavoriteContentSerializer(item)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK
                )
            except models.FavoriteContent.DoesNotExist:
                return Response(
                    {"status": "error", "data": "FavoriteContent not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        items = models.FavoriteContent.objects.all()
        serializer = serializers.FavoriteContentSerializer(items, many=True)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def post(self, request, id=None):
        serializer = serializers.FavoriteContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, id=None):
        try:
            item = models.FavoriteContent.objects.get(id=id)
            serializer = serializers.FavoriteContentSerializer(
                item, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"status": "error", "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except models.FavoriteContent.DoesNotExist:
            return Response(
                {"status": "error", "data": "FavoriteContent not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, id=None):
        item = models.FavoriteContent.objects.filter(id=id)
        print(item)
        item.delete()
        return Response(
            {"status": "success", "data": "Item Deleted"}
        )


class MovieMakersViewset(APIView):
    def get(self, request, id=None):
        if id:
            try:
                item = models.MovieMakers.objects.get(id=id)
                serializer = serializers.MovieMakersSerializer(item)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK
                )
            except models.MovieMakers.DoesNotExist:
                return Response(
                    {"status": "error", "data": "MovieMakers not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        items = models.MovieMakers.objects.all()
        serializer = serializers.MovieMakersSerializer(items, many=True)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def post(self, request, id=None):
        serializer = serializers.MovieMakersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request, id=None):
        try:
            item = models.MovieMakers.objects.get(id=id)
            serializer = serializers.MovieMakersSerializer(
                item, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"status": "error", "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except models.MovieMakers.DoesNotExist:
            return Response(
                {"status": "error", "data": "MovieMakers not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, id=None):
        item = models.MovieMakers.objects.filter(id=id)
        print(item)
        item.delete()
        return Response(
            {"status": "success", "data": "Item Deleted"}
        )

# def RegisterUser(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(email=email, password=password)
#             login(request, user)
#             return redirect('landing-page')
#     else:
#         form = UserRegisterForm()
#     return render(request, "Register.html", {'form':form})

class UserLoginViewset(APIView):

    def post(self, request, id=None):
        username = request.data.get('email')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = models.UserInfo.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserLogoutViewset(APIView):

    def post(self, request, id=None):
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
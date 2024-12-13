from rest_framework import status
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator
import logging

# Set up logging
logger = logging.getLogger(__name__)


class UserInfoViewset(APIView):
    def get(self, id=None):
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

    def post(self, request):
        if 'logout' in request.data:
            logout(request)
            return Response({'success': True})
            
        # Check if this is a login request
        if 'login' in request.data:
            try:
                email = request.data.get('email')
                password = request.data.get('password')

                if not email or not password:
                    return Response({
                        'success': False,
                        'message': 'Email and password are required'
                    }, status=status.HTTP_400_BAD_REQUEST)

                # Use email as username for authentication
                user = authenticate(request, username=email, password=password)
                
                if user is not None:
                    login(request, user)
                    return Response({
                        'success': True,
                        'user_id': user.id
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        'success': False,
                        'message': 'Invalid credentials'
                    }, status=status.HTTP_401_UNAUTHORIZED)

            except Exception as e:
                logger.exception("Login error")
                return Response({
                    'success': False,
                    'message': str(e)
                }, status=status.HTTP_400_BAD_REQUEST)

        # If not a login request, handle registration as before
        logger.info("Received user creation request")
        logger.debug(f"Request data: {request.data}")

        try:
            # Extract data from request
            data = {
                'username': request.data.get('email'),  # Using email as username
                'email': request.data.get('email'),
                'firstname': request.data.get('first_name'),
                'lastname': request.data.get('last_name'),
                'phoneNo': request.data.get('phone_number'),
                'password': request.data.get('password')
            }

            # Validate required fields
            required_fields = ['email', 'password']
            missing_fields = [field for field in required_fields if not data.get(field)]
            if missing_fields:
                return Response({
                    'success': False,
                    'message': f"Missing required fields: {', '.join(missing_fields)}"
                }, status=status.HTTP_400_BAD_REQUEST)

            # Create user
            user = models.UserInfo.objects.create_user(
                email=data['email'],
                username=data['username'],
                password=data['password'],
                firstname=data.get('firstname', ''),
                lastname=data.get('lastname', ''),
                phoneNo=data.get('phoneNo')
            )

            login(request, user)
            return Response({
                'success': True,
                'user_id': user.id
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            logger.exception("Registration error")
            return Response({
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

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
        item = models.UserInfo.objects.filter(id=id)
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

        #pagination
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 9)
        paginator = Paginator(items, page_size)

        try:
            paginated_items = paginator.page(page)
        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = serializers.ContentSerializer(paginated_items, many=True)
        return Response(
            {"status": "success", "data": serializer.data,
            "pagination":{
                    "current_page": paginated_items.number,
                    "total_pages": paginator.num_pages,
                    "total_items": paginator.count
                }
            },
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
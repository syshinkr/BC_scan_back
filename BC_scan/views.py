from django.db.models import query
from django.http.response import Http404
from rest_framework.response import Response
from BC_scan.models import BusinessCard, User
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .serializers import UserSerializer, BusinessCardSerializer


class UserBusinessCardListView(APIView):
    def get_object(self, email):
        try:
            user = User.objects.get(email=email)
            user_id = user.id

            return BusinessCard.objects.get(user=user_id)
        except User.DoesNotExist or BusinessCard.DoesNotExist:
            raise Http404


    def get(self, request, email, format=None):
        queryset = self.get_object(email=email)
        serializer = BusinessCardSerializer(queryset)
        return Response(serializer.data)

class BusinessCardDetailView(APIView):
    def get_object(self, id):
        try:
            return BusinessCard.objects.get(id=id)
        except User.DoesNotExist or BusinessCard.DoesNotExist:
            raise Http404


    def get(self, request, id, format=None):
        queryset = self.get_object(id=id)
        serializer = BusinessCardSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        queryset = self.get_object(id=id)
        serializer = BusinessCardSerializer(queryset, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        queryset = self.get_object(id=id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# list
class UserView(viewsets.ModelViewSet):
    email = None
    # queryset = User.objects.filter(email__exact=email)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(APIView):
    def get_object(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, email, format=None):
        queryset = self.get_object(email=email)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, email, format=None):
        queryset = self.get_object(email=email)
        serializer = UserSerializer(queryset, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, email, format=None):
        queryset = self.get_object(email=email)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

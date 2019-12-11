from django.http import HttpResponse, JsonResponse
from rest_framework import response, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from foundations.models import Category, Item, Favorite
from api.serializers import CategorySerializer, ItemSerializer

class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.filter(is_hidden=False).order_by('name')

        return queryset

class ItemListAPI(generics.ListAPIView):

    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.filter(is_hidden=False).order_by('name')

        return queryset

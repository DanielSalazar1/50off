from django.http import HttpResponse, JsonResponse
from rest_framework import response, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from foundations.models import UserLocation, Category, Item, Images, Favorite
from api.serializers import CategorySerializer, ItemSerializer
from api.serializers import ImagesSerializer, UserLocationSerializer
# FavoritesSerializer

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

class ImagesListAPI(generics.ListAPIView):

    serializer_class = ImagesSerializer

    def get_queryset(self):
        queryset = Images.objects.get("images")

        return queryset



# class FavoritesListAPI(django_filters.FilterSet):  #(generics.ListAPIView)

## CODE with help from : https://stackoverflow.com/questions/29929178/importerror-no-module-named-django-filters

    # queryset = Favorite.objects.all()
    # serializer_class = FavoritesSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = [
    #     'name',
    #     'original_price',
    #     'discounted_price',
    #     'percent_off',
    #     'serial',
    #     'company_name',
    #     'adress',
    #     'country',
    #     'province',
    #     'city',
    #     'is_hidden',
    #     ]

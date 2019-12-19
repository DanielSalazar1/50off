from django.http import HttpResponse, JsonResponse
from rest_framework import response, views, status
from rest_framework import generics

from foundations.models import UserLocation, Category, Item, Images, Favorite
from api.serializers import CategorySerializer, ItemSerializer, ImagesSerializer, UserLocationSerializer


## CODE with the help of Juby Varughese ##
## https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-query-parameters

class UserLocationAPI(generics.ListAPIView):

    serializer_class = UserLocationSerializer

    def get_queryset(self):
        user_location = self.request.query_params.get('country', 'province', 'city', None)

        queryset = UserLocation.objects.filter(user=self.request.user)

        if attribute_name is not None:
            queryset = queryset.filter(user_location=user_location) # (location = self.request.(city, province, country))
            return queryset

from rest_framework import status, views, response
from django.shortcuts import render


class PageLoad(views.APIView):
    def get(self, request):
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'version': '3',
            }
        );

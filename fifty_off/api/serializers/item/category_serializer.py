from rest_framework import serializers


class CategorySerializer(serializers.Serializer):

    name = serializers.CharField()
    id = serializers.IntegerField()
    is_hidden = serializers.BooleanField()

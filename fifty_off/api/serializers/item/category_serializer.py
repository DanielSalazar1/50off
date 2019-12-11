from rest_framework import serializers


class CategorySerializer(serializers.Serializer):

    name = serializers.CharField()
    is_hidden = serializers.BooleanField()
    id = serializers.IntegerField()

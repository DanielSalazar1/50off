from rest_framework import serializers

class ImagesSerializer(serializers.Serializer):

    images = serializers.ImageField()
    is_online = serializers .BooleanField()

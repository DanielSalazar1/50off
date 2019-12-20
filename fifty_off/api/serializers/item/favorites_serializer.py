from rest_framework import serializers

class FavoritesSerializer(serializers.Serializer):

    name = serializers.CharField()
    original_price = serializers.FloatField()
    discounted_price = serializers.FloatField()
    percent_off = serializers.FloatField()
    serial = serializers.UUIDField()
    company_name = serializers.CharField()
    adress = serializers.CharField()
    country = serializers.CharField()
    province = serializers.CharField()
    city = serializers.CharField()
    # image = serializers.ImageField(upload_to='images/', blank=True, null=True,)
    is_hidden = serializers.BooleanField()
    is_online = serializers.BooleanField()

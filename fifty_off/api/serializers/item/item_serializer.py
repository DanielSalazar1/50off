from rest_framework import serializers


class ItemSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    serial = serializers.UUIDField()
    is_hidden = serializers.BooleanField()
    original_price = serializers.FloatField()
    discounted_price = serializers.FloatField()
    percent_off = serializers.FloatField()
    company_name = serializers.CharField()
    adress = serializers.CharField()
    country = serializers.CharField()
    province = serializers.CharField()
    city = serializers.CharField()

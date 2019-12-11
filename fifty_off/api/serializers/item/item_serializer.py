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
    address = serializers.CharField()
    is_online = serializers.BooleanField()
    country = serializers.CharField()
    province = serializers.CharField()
    city = serializers.CharField()
    # photo = serializers.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True,)

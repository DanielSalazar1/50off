from rest_framework import serializers


class ItemSerializer(serializers.Serializer):

    name = serializers.CharField()
    is_hidden = serializers.BooleanField()
    original_price = serializers.FloatField()
    discounted_price = serializers.FloatField()
    percent_off = serializers.FloatField()
    serial = serializers.UUIDField()
    id = serializers.IntegerField()
    # photo = serializers.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True,)

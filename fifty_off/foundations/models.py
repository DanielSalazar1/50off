import uuid
from django.db import models
from django.contrib.auth.models import User

class UserLocation(models.Model):
    country = models.CharField(max_length=70)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=False, blank=True,)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    original_price = models.FloatField()
    discounted_price = models.FloatField()
    percent_off = models.FloatField()
    serial = models.UUIDField(default=uuid.uuid4, editable=False,)
    company_name = models.CharField(max_length=255,)
    adress = models.CharField(max_length=255, blank=True, null=True,)
    country = models.CharField(max_length=255,)
    province = models.CharField(max_length=255, blank=True, null=True,)
    city = models.CharField(max_length=255,)
    # image = models.ImageField(upload_to='images/', blank=True, null=True,)
    is_hidden = models.BooleanField(default=False, blank=True,)
    # is_online = models.BooleanField(default=False, blank=True,)

    # TO DO
    # WHERE WOULD I BUY THIS PRODUCT AT. (COUNTRY, PROVINCE, CITY)
    #which company is it from?
    #How do I know if the purchase is on line or physical (is_online=BooleanField)

    def __str__(self):
        return self.name

    # CODE BELOW TAKEN FROM: https://stackoverflow.com/questions/35884951/upload-images-as-raw-data-in-django-rest-framework

class Images(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete = models.CASCADE
    )
    images = models.ImageField(upload_to='images/', blank=False, null=False, default='SOME IMAGE')
    is_online = models.BooleanField(default=False, blank=True,)


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )

    images = models.ForeignKey(
        Images,
        on_delete = models.CASCADE
    )

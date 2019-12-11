import uuid
from django.db import models
from django.contrib.auth.models import User


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
    serial = models.UUIDField(default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True,)

    is_hidden = models.BooleanField(default=False, blank=True,)
    is_online = models.BooleanField(default=False, blank=True,)

    # TO DO
    # WHERE WOULD I BUY THIS PRODUCT AT. (COUNTRY, PROVINCE, CITY)
    #which company is it from?
    #How do I know if the purchase is on line or physical (is_online=BooleanField)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )

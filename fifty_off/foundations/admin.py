from django.contrib import admin

from foundations.models import Item, Favorite, Category

# Register your models here.

admin.site.register(Item)
admin.site.register(Favorite)
admin.site.register(Category)

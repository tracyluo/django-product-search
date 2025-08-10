from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.tag import Tag

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)

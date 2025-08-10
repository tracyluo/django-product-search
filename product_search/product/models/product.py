from django.db import models
from .category import Category
from .tag import Tag

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
      Category,
      on_delete = models.PROTECT,
      related_name = 'products',
      null=True,
      blank=True
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

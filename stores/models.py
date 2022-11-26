from django.db import models
from cart.models import Cart


class Shop(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Category (models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, null='Категория')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


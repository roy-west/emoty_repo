from django.db import models
# from cart.models import Cart


class Shop(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.title


class Category (models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, null='Категория')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # cart = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Supplies(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_supplies')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='supplies')
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'

    def __str__(self):
        return f"Количество поставленного товара - {self.product} в магазин {self.shop} составляет {self.quantity} шт."


class Sales(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='sales')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sales')
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

    def __str__(self):
        return f"Количество проданного товара - {self.product} составляет {self.quantity} шт."
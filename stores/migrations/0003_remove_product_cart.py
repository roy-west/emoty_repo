# Generated by Django 4.1.3 on 2022-11-25 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_product_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cart',
        ),
    ]
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Shop(models.Model):
    name=models.TextField()
    icon=models.ImageField('Ikona sklepu', upload_to='products/%Y/%m/%d')
    objects=models.Manager()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.TextField('Nazwa Produktu', max_length=200)
    slug = models.SlugField('Odnośnik', unique=True, max_length=100)
    icon = models.ImageField('Ikona Produktu', upload_to='products/%Y/%m/%d')
    promotion = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.name

class ProductShop(models.Model):
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    def __str__(self):
        return self.product.name

class UserLike(models.Model):
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.shop + self.product + self.user

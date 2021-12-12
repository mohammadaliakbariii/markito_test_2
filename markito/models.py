from django.db import models
from accounts.models import CustomUser


# Create your models here.


class Channel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=15,unique=True)


    class Meta:
        verbose_name_plural = 'channels'
    def __str__(self):
        return self.name

class Store(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    channel = models.ManyToManyField(Channel)
    name = models.CharField(max_length=50,unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name



class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Products(models.Model):
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    count = models.PositiveIntegerField(default=0)
    buy_price = models.DecimalField(max_digits=50, decimal_places=2)
    sell_price = models.DecimalField(max_digits=50, decimal_places=2)
    side_costs = models.DecimalField(max_digits=50, decimal_places=2)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
    def profit(self):
        pass







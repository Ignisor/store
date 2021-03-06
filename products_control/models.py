from __future__ import unicode_literals
from django.db import models
from django import template
from datetime import date
import requests
import json

register = template.Library()


class Brand(models.Model):
    """
    Brand model
    """
    name = models.CharField(max_length=256, default='NoName')
    slug = models.SlugField()

    def __unicode__(self):
        return self.name


class Category(models.Model):
    """
    Category model
    """
    name = models.CharField(max_length=256, default='NoName')
    slug = models.SlugField()

    def __unicode__(self):
        return self.name


class Product(models.Model):
    """
    Product model
    """
    brand = models.ForeignKey(Brand, related_name='products', null=True)
    category = models.ForeignKey(Category, related_name='products', null=True)
    barcode = models.IntegerField(primary_key=True, unique=True) # unique barcode of product as primary key
    name = models.CharField(max_length=256, default='NoName')
    image = models.ImageField(upload_to='products_images/', null=True, blank=True)
    price = models.FloatField(default=0.00)

    def __unicode__(self):
        return self.name

    @property
    def price_in_uah(obj):
        # if no exchange rate object exist in database - create it
        if len(ExchangeRate.objects.all()) < 1:
            ex_rate = ExchangeRate(buying = 0, selling = 0, last_update = date.today())
            ex_rate.save()
            ex_rate.update_rate()

        ex_rate = ExchangeRate.objects.all()[0]

        return obj.price * ex_rate.get_buying()


class ExchangeRate(models.Model):
    """
    Model for storing rate of exchange
    """
    buying = models.FloatField()
    selling = models.FloatField()
    last_update = models.DateField()

    def get_buying(self):
        # check is rate was updated today
        if date.today() > self.last_update:
            self.update_rate()
        return self.buying

    def get_selling(self):
        # check is rate was updated today
        if date.today() > self.last_update:
            self.update_rate()
        return self.selling

    def update_rate(self):
        # get exchange rate from "obmenka.kharkov.ua"
        req = requests.get('https://obmenka.kharkov.ua/rate/list')

        if req.status_code == 200:
            j = json.loads(req.content)

            self.selling = j[0]['amountRetailTo']
            self.buying = j[0]['amountRetailFrom']
            self.last_update = date.today()

            self.save()

            return True

        else: return False



class Amount(models.Model):
    """
    Model for amount of some product
    """
    product = models.OneToOneField(Product, related_name='amount')
    num = models.IntegerField()

    def __unicode__(self):
        return self.product.name + ": " + str(self.num)


class Log(models.Model):
    """
    Model for logging changes in products
    """
    product = models.ForeignKey(Product, related_name='logs')
    d_amount = models.IntegerField() # delta amount = old_amount - new_amount
    time = models.DateTimeField(auto_now_add=True) # date and time of changes
    type = models.CharField(max_length=16)


class Provider(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name


class Order(models.Model):
    provider = models.ForeignKey(Provider, related_name='orders')
    product = models.ForeignKey(Product, related_name='orders')
    ordered_amount = models.IntegerField()
    delivered_amount = models.IntegerField(blank=True, null=True)
    accepted = models.BooleanField(default=False)
    creation_date = models.DateField(auto_now_add=True)
    deliver_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.provider.name + ': ' + self.product.name + '(' + str(self.ordered_amount) + ')'

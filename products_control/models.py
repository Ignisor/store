from __future__ import unicode_literals

from django.db import models


class Brand(models.Model):
    '''
    Brand model
    '''
    name = models.CharField(max_length=256, default='NoName')
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Category(models.Model):
    '''
    Category model
    '''
    name = models.CharField(max_length=256, default='NoName')
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product model
    """
    brand = models.ForeignKey(Brand, related_name='products', null=True)
    category = models.ForeignKey(Category, related_name='products', null=True)
    barcode = models.IntegerField(primary_key=True, unique=True) # unique barcode of product as primary key
    name = models.CharField(max_length=256, default='NoName')
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.name


class Amount(models.Model):
    """
    Model for amount of some product
    """
    TYPES = (
        ('+', 'add'),
        ('-', 'remove'),
    )

    product = models.OneToOneField(Product, related_name='amount')
    num = models.IntegerField()
    type = models.CharField(max_length=16, choices=TYPES, default=TYPES[0])

    def __str__(self):
        return self.product.name + ": " + str(self.num)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     old_num = self.num
    #
    #     super(Amount, self).save(force_insert=False, force_update=False, using=None,
    #          update_fields=None)
    #
    #     new_num = self.num()
    #     log = Log(product=self.product,
    #               d_amount=old_num - new_num,
    #               time = )


class Log(models.Model):
    """
    Mdel for loggin changes in products
    """
    product = models.ForeignKey(Product, related_name='logs')
    d_amount = models.IntegerField() # delta amount = old_amount - new_amount
    time = models.DateTimeField() # date and time of changes

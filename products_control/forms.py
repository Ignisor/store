from .models import Product, Brand, Category, Log, Amount, Order
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def save(self, commit=True):
        product = super(ProductForm, self).save(commit)

        # create Amount model with 0 amount for this prduct
        amount = Amount(product=product, num=0)

        amount.save()

        return product


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class IncomeForm(forms.ModelForm):
    """
    Form for adding some amount to product, and create changes log
    """
    product = forms.IntegerField()

    class Meta:
        model = Log
        fields = ['product', 'd_amount']

    def clean_product(self):
        # get product by barcode
        return Product.objects.get(pk=self.data.get('product'))

    def save(self, commit=True):
        # create log, and change amount of product
        log = super(IncomeForm, self).save(commit)
        log.type = 'add'
        log.save()

        product = self.cleaned_data.get('product')

        amount = product.amount
        amount.num += self.cleaned_data.get('d_amount')
        amount.save()

        return log


class OutcomeForm(forms.ModelForm):
    """
    Form for removing some amount to product, and create changes log
    """
    product = forms.IntegerField()

    class Meta:
        model = Log
        fields = ['product', 'd_amount']

    def clean_product(self):
        # get product by barcode
        return Product.objects.get(pk=self.data.get('product'))

    def save(self, commit=True):
        # create log, and change amount of product
        log = super(OutcomeForm, self).save(commit)
        log.type = 'remove'
        log.save()

        product = self.cleaned_data.get('product')

        amount = product.amount
        amount.num -= self.cleaned_data.get('d_amount')
        amount.save()

        return log


class OrderForm(forms.ModelForm):
    """
    Form for creating new order
    """
    product = forms.IntegerField()

    class Meta:
        model = Order
        fields = ['product', 'provider', 'ordered_amount']

    def clean_product(self):
        # get product by barcode
        return Product.objects.get(pk=self.data.get('product'))
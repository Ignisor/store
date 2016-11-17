from .models import Product, Brand, Category, Log, Amount, Order
from django import forms
from annoying.functions import get_object_or_None


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def save(self, commit=True):
        product = super(ProductForm, self).save(commit)
        amount = Amount(product=product,
                        num=0,
                        )

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
    product = forms.IntegerField()

    class Meta:
        model = Log
        fields = ['product', 'd_amount']

    def clean_product(self):
        return Product.objects.get(pk=self.data.get('product'))

    def save(self, commit=True):
        log = super(IncomeForm, self).save(commit)

        log.type = 'add'

        log.save()

        product = self.cleaned_data.get('product')

        amount = product.amount
        amount.num += self.cleaned_data.get('d_amount')

        amount.save()
        return log


class OutcomeForm(forms.ModelForm):
    product = forms.IntegerField()

    class Meta:
        model = Log
        fields = ['product', 'd_amount']

    def clean_product(self):
        return Product.objects.get(pk=self.data.get('product'))

    def save(self, commit=True):
        log = super(OutcomeForm, self).save(commit)

        log.type = 'remove'

        log.save()

        product = self.cleaned_data.get('product')

        amount = product.amount
        amount.num -= self.cleaned_data.get('d_amount')

        amount.save()
        return log


class OrderForm(forms.ModelForm):
    product = forms.IntegerField()

    class Meta:
        model = Order
        fields = ['product', 'provider', 'ordered_amount']

    def clean_product(self):
        return Product.objects.get(pk=self.data.get('product'))

    # def save(self, commit=True):
    #     order = super(OutcomeForm, self).save(commit)
    #     return order
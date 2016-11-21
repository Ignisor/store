from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from annoying.functions import get_object_or_None

from .forms import ProductForm, BrandForm, CategoryForm, IncomeForm, OutcomeForm, OrderForm
from .models import Brand, Product, Category, Log, Provider, Order


def index(request):
    return render(request, 'index.html')


# Views to create models
class ProductCreateView(CreateView):
    template_name = 'products_control/add_product.html'
    form_class = ProductForm
    success_url = '/products/'


class BrandCreateView(CreateView):
    template_name = 'products_control/add_brand.html'
    form_class = BrandForm
    success_url = '/brands/'


class CategoryCreateView(CreateView):
    template_name = 'products_control/add_category.html'
    form_class = CategoryForm
    success_url = '/categories/'


class ProviderCreateView(CreateView):
    template_name = 'products_control/add_provider.html'
    model = Provider
    fields = '__all__'
    success_url = '/providers/'


# Views to get models
class ProductsListView(ListView):
    model = Product

    def get_queryset(self):
        if self.kwargs.get('brand_name') is not None:
            self.brand = get_object_or_None(Brand, slug=self.kwargs.get('brand_name'))
            return Product.objects.filter(brand=self.brand)
        elif self.kwargs.get('category_name') is not None:
            self.category = get_object_or_None(Category, slug=self.kwargs.get('category_name'))
            return Product.objects.filter(category=self.category)
        else:
            return Product.objects.all()


class BrandsListView(ListView):
    model = Brand


class CategoriesListView(ListView):
    model = Category


class LogListView(ListView):
    model = Log


class ProviderListView(ListView):
    model = Provider


class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        if self.kwargs.get('provider_name') is not None:
            provider = get_object_or_None(Provider, slug=self.kwargs.get('provider_name'))
            return Order.objects.filter(provider=provider)
        else:
            return None


class BadOrderListView(ListView):
    model = Order

    template_name = 'products_control/bad_order_list.html'

    def get_queryset(self):
        objects = Order.objects.filter(accepted=True)
        for obj in objects:
            if obj.delivered_amount == obj.ordered_amount:
                objects = objects.exclude(id=obj.id)

        return objects


def product_view(request, product_barcode):
    product = get_object_or_404(Product, pk = product_barcode)
    context = {
        'product' : product
    }

    return render(request, 'products_control/product.html', context)


# Views to update models
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = '/products/'

    # def post(self, request, *args, **kwargs):
    #     response = super(ProductUpdateView, self).post(self, request, *args, **kwargs)
    #     self.success_url = '/product/{pk}/'.format(pk=self.object.barcode)
    #     return response


class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = '/categories/'


class BrandUpdateView(UpdateView):
    model = Brand
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = '/brands/'


class ProviderUpdateView(UpdateView):
    model = Provider
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = '/providers/'


class OrderConfirmView(UpdateView):
    model = Order
    fields = ['delivered_amount', 'deliver_date']
    template_name_suffix = '_confirm'
    success_url = '/providers/'

    def form_valid(self, form):
        self.object.accepted = True
        self.object.save()

        obj = super(OrderConfirmView, self).form_valid(form)

        self.object.product.amount.num += self.object.delivered_amount
        self.object.product.amount.save()

        return obj


# Views to delete models
class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/products/'
    template_name_suffix = '_delete'


class BrandDeleteView(DeleteView):
    model = Brand
    success_url = '/brands/'
    template_name_suffix = '_delete'


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/categories/'
    template_name_suffix = '_delete'


class ProviderDeleteView(DeleteView):
    model = Provider
    success_url = '/providers/'
    template_name_suffix = '_delete'


# Views for income and outcome
class IncomeFormView(FormView):
    template_name = 'products_control/income.html'
    form_class = IncomeForm
    success_url = '/products/'

    def form_valid(self, form):
        form.save()
        return super(IncomeFormView, self).form_valid(form)


class OutcomeFormView(FormView):
    template_name = 'products_control/outcome.html'
    form_class = OutcomeForm
    success_url = '/products/'

    def form_valid(self, form):
        form.save()
        return super(OutcomeFormView, self).form_valid(form)


# Create order view
class OrderFormView(FormView):
    template_name = 'products_control/new_order.html'
    form_class = OrderForm
    success_url = '/new_order/'

    def form_valid(self, form):
        form.save()
        return super(OrderFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OrderFormView, self).get_context_data(**kwargs)
        providers_dict = {}
        for provider in Provider.objects.all():
            providers_dict[str(provider.id)] = provider.name.encode('ascii', 'xmlcharrefreplace')

        context['providers'] = providers_dict
        return context
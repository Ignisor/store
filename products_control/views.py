from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from annoying.functions import get_object_or_None

from .forms import ProductForm, BrandForm, CategoryForm
from .models import Brand, Product, Category


def index(request):
    return render(request, 'index.html')


# Views to create models
class ProductCreateView(CreateView):
    template_name = 'products_control/add_product.html'
    form_class = ProductForm
    success_url = '/product_control/add_product/'


class BrandCreateView(CreateView):
    template_name = 'products_control/add_brand.html'
    form_class = BrandForm
    success_url = '/product_control/add_brand/'


class CategoryCreateView(CreateView):
    template_name = 'products_control/add_category.html'
    form_class = CategoryForm
    success_url = '/product_control/add_category/'


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



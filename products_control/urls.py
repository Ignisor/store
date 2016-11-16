from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from .views import ProductCreateView, BrandCreateView, CategoryCreateView, \
    BrandsListView, ProductsListView, CategoriesListView, index, product_view, \
    ProductUpdateView, BrandUpdateView, CategoryUpdateView, ProductDeleteView, \
    CategoryDeleteView, BrandDeleteView

urlpatterns = [
    url(r'^$', login_required(index), name='index'),
    url(r'^accounts/login/$', login, kwargs={'template_name': 'login.html'}, name='login'),
    url(r'^accounts/logout/$', logout,  kwargs={'next_page': '/'}, name='logout'),
    url(r'^product_control/add_product/$', login_required(ProductCreateView.as_view()), name='add_product'),
    url(r'^product_control/add_brand/$', login_required(BrandCreateView.as_view()), name='add_brand'),
    url(r'^product_control/add_category/$', login_required(CategoryCreateView.as_view()), name='add_category'),
    url(r'^brands/$', login_required(BrandsListView.as_view()), name='brands'),
    url(r'^categories/$', login_required(CategoriesListView.as_view()), name='categories'),
    url(r'^products/brand/(?P<brand_name>[\w -.]+)/$', login_required(ProductsListView.as_view()), name='products'),
    url(r'^products/category/(?P<category_name>[\w -.]+)/$', login_required(ProductsListView.as_view()), name='products'),
    url(r'^products/$', login_required(ProductsListView.as_view()), name='products'),
    url(r'^product/(?P<product_barcode>\d+)/$', login_required(product_view), name='product'),
    url(r'^product/(?P<pk>\d+)/update/$', login_required(ProductUpdateView.as_view()), name='product_update'),
    url(r'^brand/(?P<slug>[\w -.]+)/update/$', login_required(BrandUpdateView.as_view()), name='brand_update'),
    url(r'^category/(?P<slug>[\w -.]+)/update/$', login_required(CategoryUpdateView.as_view()), name='category_update'),
    url(r'^product/(?P<pk>\d+)/delete/$', login_required(ProductDeleteView.as_view()), name='product_delete'),
    url(r'^brand/(?P<slug>[\w -.]+)/delete/$', login_required(BrandDeleteView.as_view()), name='brand_update'),
    url(r'^category/(?P<slug>[\w -.]+)/delete/$', login_required(CategoryDeleteView.as_view()), name='category_update'),
]


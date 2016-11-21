from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.views import login, logout
from .views import ProductCreateView, BrandCreateView, CategoryCreateView, \
    BrandsListView, ProductsListView, CategoriesListView, index, product_view, \
    ProductUpdateView, BrandUpdateView, CategoryUpdateView, ProductDeleteView, \
    CategoryDeleteView, BrandDeleteView, IncomeFormView, OutcomeFormView, LogListView, \
    ProviderCreateView, ProviderListView, ProviderUpdateView, ProviderDeleteView, \
    OrderFormView, OrderListView, OrderConfirmView, BadOrderListView, OrderDeleteView

urlpatterns = [
    url(r'^$', login_required(index), name='index'),
    url(r'^accounts/login/$', login, kwargs={'template_name': 'login.html'}, name='login'),
    url(r'^accounts/logout/$', logout,  kwargs={'next_page': '/'}, name='logout'),
    url(r'^product_control/add_product/$', login_required(ProductCreateView.as_view()), name='add_product'),
    url(r'^product_control/add_brand/$', login_required(BrandCreateView.as_view()), name='add_brand'),
    url(r'^product_control/add_category/$', login_required(CategoryCreateView.as_view()), name='add_category'),
    url(r'^product_control/add_provider/$', login_required(ProviderCreateView.as_view()), name='add_provider'),
    url(r'^brands/$', login_required(BrandsListView.as_view()), name='brands'),
    url(r'^categories/$', login_required(CategoriesListView.as_view()), name='categories'),
    url(r'^logs/$', login_required(LogListView.as_view()), name='logs'),
    url(r'^products/brand/(?P<brand_name>[\w -.]+)/$', login_required(ProductsListView.as_view()), name='products'),
    url(r'^products/category/(?P<category_name>[\w -.]+)/$', login_required(ProductsListView.as_view()), name='products'),
    url(r'^products/$', login_required(ProductsListView.as_view()), name='products'),
    url(r'^product/(?P<product_barcode>\d+)/$', login_required(product_view), name='product'),
    url(r'^product/(?P<pk>\d+)/update/$', login_required(ProductUpdateView.as_view()), name='product_update'),
    url(r'^brand/(?P<slug>[\w -.]+)/update/$', login_required(BrandUpdateView.as_view()), name='brand_update'),
    url(r'^category/(?P<slug>[\w -.]+)/update/$', login_required(CategoryUpdateView.as_view()), name='category_update'),
    url(r'^product/(?P<pk>\d+)/delete/$', login_required(ProductDeleteView.as_view()), name='product_delete'),
    url(r'^brand/(?P<slug>[\w -.]+)/delete/$', login_required(BrandDeleteView.as_view()), name='brand_delete'),
    url(r'^category/(?P<slug>[\w -.]+)/delete/$', login_required(CategoryDeleteView.as_view()), name='category_delete'),
    url(r'^order/(?P<pk>[\w -.]+)/delete/$', login_required(OrderDeleteView.as_view()), name='order_delete'),
    url(r'^providers/$', login_required(ProviderListView.as_view()), name='providers'),
    url(r'^providers/(?P<provider_name>[\w -.]+)/$', login_required(OrderListView.as_view()), name='orders'),
    url(r'^providers/(?P<slug>[\w -.]+)/update/$', login_required(ProviderUpdateView.as_view()), name='provider_update'),
    url(r'^providers/(?P<slug>[\w -.]+)/delete/$', login_required(ProviderDeleteView.as_view()), name='provider_delete'),
    url(r'^new_order/$', login_required(OrderFormView.as_view()), name='new_order'),
    url(r'^confirm_order/(?P<pk>\d+)/$', login_required(OrderConfirmView.as_view()), name='confirm_order'),
    url(r'^bad_orders/$', login_required(BadOrderListView.as_view()), name='bad_orders'),
    url(r'^income/$', login_required(IncomeFormView.as_view()), name='income'),
    url(r'^outcome/$', login_required(OutcomeFormView.as_view()), name='outcome'),
]
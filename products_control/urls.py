from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout
from .views import ProductCreateView, BrandCreateView, CategoryCreateView, \
    BrandsListView, ProductsListView, CategoriesListView, index, product_view, \
    ProductUpdateView, BrandUpdateView, CategoryUpdateView, ProductDeleteView, \
    CategoryDeleteView, BrandDeleteView, IncomeFormView, OutcomeFormView, LogListView, \
    ProviderCreateView, ProviderListView, ProviderUpdateView, ProviderDeleteView, \
    OrderFormView, OrderListView, OrderConfirmView, BadOrderListView, OrderDeleteView, \
    excel_export_income

urlpatterns = [
    # index(home) page
    url(r'^$', login_required(index),
        name ='index'),
    # header
    url(r'^header.html', TemplateView.as_view(template_name='header.html')),
    # default django login page
    url(r'^accounts/login/$', login, kwargs={'template_name': 'login.html'},
        name='login'),
    # default django logout page
    url(r'^accounts/logout/$', logout,  kwargs={'next_page': '/'},
        name='logout'),
    # product adding
    url(r'^product_control/add_product/$', login_required(ProductCreateView.as_view()),
        name='add_product'),
    # brand adding
    url(r'^product_control/add_brand/$', login_required(BrandCreateView.as_view()),
        name='add_brand'),
    # category adding
    url(r'^product_control/add_category/$', login_required(CategoryCreateView.as_view()),
        name='add_category'),
    # provider adding
    url(r'^product_control/add_provider/$', login_required(ProviderCreateView.as_view()),
        name='add_provider'),
    # brands list
    url(r'^brands/$', login_required(BrandsListView.as_view()),
        name='brands'),
    # categories list
    url(r'^categories/$', login_required(CategoriesListView.as_view()),
        name='categories'),
    # income and outcome logs
    url(r'^logs/$', login_required(LogListView.as_view()),
        name='logs'),
    # list of products, filtered by brand
    url(r'^products/brand/(?P<brand_name>[\w -.]+)/$', login_required(ProductsListView.as_view()),
        name='products_by_brand'),
    # list of products, filtered by category
    url(r'^products/category/(?P<category_name>[\w -.]+)/$', login_required(ProductsListView.as_view()),
        name='products_by_category'),
    # list of all products
    url(r'^products/$', login_required(ProductsListView.as_view()),
        name='products'),
    # product view
    url(r'^product/(?P<product_barcode>\d+)/$', login_required(product_view),
        name='product'),
    # change product
    url(r'^product/(?P<pk>\d+)/update/$', login_required(ProductUpdateView.as_view()),
        name='product_update'),
    # change brand
    url(r'^brand/(?P<slug>[\w -.]+)/update/$', login_required(BrandUpdateView.as_view()),
        name='brand_update'),
    # change category
    url(r'^category/(?P<slug>[\w -.]+)/update/$', login_required(CategoryUpdateView.as_view()),
        name='category_update'),
    # delete product
    url(r'^product/(?P<pk>\d+)/delete/$', login_required(ProductDeleteView.as_view()),
        name='product_delete'),
    # delete brand
    url(r'^brand/(?P<slug>[\w -.]+)/delete/$', login_required(BrandDeleteView.as_view()),
        name='brand_delete'),
    # delete category
    url(r'^category/(?P<slug>[\w -.]+)/delete/$', login_required(CategoryDeleteView.as_view()),
        name='category_delete'),
    # delete order
    url(r'^order/(?P<pk>[\w -.]+)/delete/$', login_required(OrderDeleteView.as_view()),
        name='order_delete'),
    # providers list
    url(r'^providers/$', login_required(ProviderListView.as_view()),
        name='providers'),
    # orders list, always filtered by some provider
    url(r'^providers/(?P<provider_name>[\w -.]+)/$', login_required(OrderListView.as_view()),
        name='orders'),
    # change provider
    url(r'^providers/(?P<slug>[\w -.]+)/update/$', login_required(ProviderUpdateView.as_view()),
        name='provider_update'),
    # delete provider
    url(r'^providers/(?P<slug>[\w -.]+)/delete/$', login_required(ProviderDeleteView.as_view()),
        name='provider_delete'),
    # place new order
    url(r'^new_order/$', login_required(OrderFormView.as_view()),
        name='new_order'),
    # confirm order
    url(r'^confirm_order/(?P<pk>\d+)/$', login_required(OrderConfirmView.as_view()),
        name='confirm_order'),
    # list of "bad" orders. Orders that confirmed but delivered amount not equals to ordered amount
    url(r'^bad_orders/$', login_required(BadOrderListView.as_view()),
        name='bad_orders'),
    # add some amount to product
    url(r'^income/$', login_required(IncomeFormView.as_view()),
        name='income'),
    # remove some amount from product
    url(r'^outcome/$', login_required(OutcomeFormView.as_view()),
        name='outcome'),
    # export income to excel file
    url(r'^export/income/$', login_required(excel_export_income),
        name='export_income'),
]
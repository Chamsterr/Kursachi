from django.contrib import admin
from django.urls import path

from .views import index, category, product


app_name = "store"
urlpatterns = [
    path('', index, {'template_name': 'store/index.html'}, name='index'),
    path('info/', index, {'template_name': 'store/info.html'}, name='info'),
    path('catalog/<int:category_id>/', category,
         {'template_name': 'store/catalog.html'}, name='catalog'),
    path('product/<int:product_id>/', product,
         {'template_name': 'store/product.html'}, name='product')
]

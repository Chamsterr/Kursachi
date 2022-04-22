from django.shortcuts import render, get_object_or_404
from .models import Product, Category

categories = Category.objects.order_by().all()
products_preview = {x: Product.objects.filter(category=x)[:3]
                    for x in categories}


def index(request, template_name):
    context = {
        'products_preview': products_preview,
    }
    return render(request, template_name, context)


def category(request, template_name, category_id=None):
    products_in = Product.objects.filter(category=category_id)
    current_category = Category.objects.get(pk=category_id)
    context = {
        'products_in': products_in,
        'categories': categories,
        'products_preview': products_preview,
        'current_category': current_category,
    }
    return render(request, template_name, context)


def product(request, template_name, product_id):
    product_ = Product.objects.get(pk=product_id)
    context = {
        'products_preview': products_preview,
        'product': product_,
    }
    return render(request, template_name, context)
from django.shortcuts import render
from .models import Product, Category
from cart.forms import CartAddProductForm

categories = Category.objects.order_by().all()
products_preview = {x: Product.objects.filter(category=x)[:3]
                    for x in categories}


def index(request, template_name):
    most_popular = {x: Product.objects.filter(category=x)[:1]
                    for x in categories[:3]}
    context = {
        'products_preview': products_preview,
        'most_popular': most_popular,
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


def all_products(request, template_name):
    products_in = Product.objects.all()
    context = {
        'products_in': products_in,
        'categories': categories,
        'products_preview': products_preview,
    }
    return render(request, template_name, context)


def product(request, template_name, product_id):
    product_ = Product.objects.get(pk=product_id)
    cart_product_form = CartAddProductForm()
    context = {
        'products_preview': products_preview,
        'product': product_,
        'cart_product_form': cart_product_form,
    }
    return render(request, template_name, context)
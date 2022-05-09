from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm

categories = Category.objects.order_by().all()
products_preview = {x: Product.objects.filter(category=x)[:3]
                    for x in categories}


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['_'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    content = {
        'cart': cart,
        'categories': categories,
        'products_preview': products_preview,
    }
    return render(request, 'cart/detail.html', content)
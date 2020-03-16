from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template

from .models import Product, SubCategory
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = SubCategory.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(SubCategory, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/index.html', {'category': category,
                                               'categories': categories,
                                               'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    extra = Product.objects.exclude(id=id).filter(category=product.category)[:4]
    cart_product_form = CartAddProductForm()
    return render(request, 'main/product_detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        'extra': extra})


def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

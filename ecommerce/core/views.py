from django.shortcuts import render, get_object_or_404
from .models import Product

from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'home.html')

def product_list(request):
    query = request.GET.get("q")
    category = request.GET.get("category")

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category__iexact=category)

    return render(request, "products.html", {
        "products": products
    })



def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

from .models import Product

def home(request):
    featured_products = Product.objects.all()[:4]  # first 4
    return render(request, "home.html", {
        "products": featured_products
    })


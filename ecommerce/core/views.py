from django.shortcuts import render, get_object_or_404
from .models import Product, Category



# Home Page — show featured products
def home(request):
    featured_products = Product.objects.all()[:4]
    return render(request, "home.html", {
        "products": featured_products
    })


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()  # fetch all categories

    search = request.GET.get("search")
    category_id = request.GET.get("category")

    if search:
        products = products.filter(name__icontains=search)

    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, "products.html", {
        "products": products,
        "categories": categories
    })




# Product Detail Page
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product_detail.html", {
        "product": product
    })

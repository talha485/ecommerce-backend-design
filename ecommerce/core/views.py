from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Product, Category, CartItem


# -----------------------
# Home Page
# -----------------------
def home(request):
    featured_products = Product.objects.all()[:4]
    return render(request, "home.html", {
        "products": featured_products
    })


# -----------------------
# Product List + Search + Category + Pagination
# -----------------------
def product_list(request):
    products = Product.objects.all().order_by("-id")
    categories = Category.objects.all()

    search = request.GET.get("search")
    if search:
        products = products.filter(name__icontains=search)

    category_id = request.GET.get("category")
    if category_id:
        products = products.filter(category_id=category_id)

    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "products.html", {
        "page_obj": page_obj,
        "categories": categories
    })


# -----------------------
# Product Detail
# -----------------------
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product_detail.html", {
        "product": product
    })


# -----------------------
# Auth — Signup/Login/Logout
# -----------------------
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {"error": "Invalid credentials"})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


# -----------------------
# Cart — Add
# -----------------------
@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("product_list")


# -----------------------
# Cart — View
# -----------------------
@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)

    for item in items:
        item.subtotal = item.product.price * item.quantity

    total = sum(item.subtotal for item in items)

    return render(request, "cart.html", {
        "items": items,
        "total": total
    })



# -----------------------
# Cart — Increase / Decrease / Remove
# -----------------------
@login_required
def cart_increase(request, id):
    item = get_object_or_404(CartItem, id=id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart')


@login_required
def cart_decrease(request, id):
    item = get_object_or_404(CartItem, id=id, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')


@login_required
def cart_remove(request, id):
    item = get_object_or_404(CartItem, id=id, user=request.user)
    item.delete()
    return redirect('cart')

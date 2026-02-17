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
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Signup
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html')

# Login
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('home')
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import CartItem, Product


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
from django.contrib.auth.decorators import login_required
from .models import CartItem

@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)

    total = 0
    for item in items:
        total += item.product.price * item.quantity

    return render(request, "cart.html", {
        "items": items,
        "total": total
    })

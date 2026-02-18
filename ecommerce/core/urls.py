from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('products/', views.product_list, name='product_list'),  # Product list
    path('products/<int:id>/', views.product_detail, name='product_detail'),  # Product detail
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.product_list, name="product_list"),
    path('products/<int:id>/', views.product_detail, name="product_detail"),
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path("cart/", views.cart_view, name="cart"),
    path("cart/increase/<int:id>/", views.cart_increase, name="cart_increase"),
    path("cart/decrease/<int:id>/", views.cart_decrease, name="cart_decrease"),
    path("cart/remove/<int:id>/", views.cart_remove, name="cart_remove"),
    path("add-to-cart/<int:id>/", views.add_to_cart, name="add_to_cart"),


]



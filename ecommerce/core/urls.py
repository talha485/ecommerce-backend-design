from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('products/', views.product_list, name='product_list'),  # Product list
    path('products/<int:id>/', views.product_detail, name='product_detail'),  # Product detail
]


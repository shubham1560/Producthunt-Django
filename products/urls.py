from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.products, name="products"),
    path('<int:product_id>', views.detail, name="productDetail"),
    
]

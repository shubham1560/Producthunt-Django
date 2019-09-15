from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.products, name="products"),
    path('<int:product_id>', views.detail, name="productDetail"),
    path('<int:product_id>/vote', views.vote, name="vote")
]

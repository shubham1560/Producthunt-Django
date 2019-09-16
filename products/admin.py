from django.contrib import admin
from .models import Product
from .models import ProductAttribute, ProductFeedback
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(ProductFeedback)


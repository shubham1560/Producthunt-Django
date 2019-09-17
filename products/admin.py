from django.contrib import admin
from .models import Product
from .models import ProductAttribute, ProductFeedback
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


class ProductFeedbackAdmin(admin.ModelAdmin):
    list_display = ('comment', 'commentedBy', 'product', 'active')


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('vote', 'product', 'voter')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(ProductFeedback, ProductFeedbackAdmin)


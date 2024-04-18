from django.contrib import admin
from core.models import CustomUser, Payment, Product, Cart, CartItem, ProductReview, Checkout, MerchantProfile, Notification


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Payment)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(MerchantProfile)
admin.site.register(Checkout)
admin.site.register(Notification)







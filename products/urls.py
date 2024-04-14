from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSets, WishlistViewSet

router = DefaultRouter()
router.register('', ProductViewSets)
router.register('wishlist', WishlistViewSet, basename='wishlist')


app_name = 'products'

urlpatterns = [
    path('', include(router.urls)),
]
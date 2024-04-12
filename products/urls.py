from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSets

router = DefaultRouter()
router.register('', ProductViewSets)


app_name = 'products'

urlpatterns = [
    path('', include(router.urls)),
]
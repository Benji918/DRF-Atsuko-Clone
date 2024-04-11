from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSets

router = DefaultRouter()
router.register('', ProfileViewSets)


app_name = 'merchant_profile'

urlpatterns = [
    path('', include(router.urls)),
]
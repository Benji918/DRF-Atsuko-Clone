from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSets

router = DefaultRouter()
router.register('', NotificationViewSets)


app_name = 'notifications'

urlpatterns = [
    path('', include(router.urls)),
]
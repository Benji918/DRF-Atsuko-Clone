from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import NotificationViewSets

router = SimpleRouter()
router.register('', NotificationViewSets)


app_name = 'notifications'

urlpatterns = [
    path('', include(router.urls)),
]

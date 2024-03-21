from django.urls import path

from .apis import (
    GoogleLoginApi,
    GoogleLoginRedirectApi,
)


app_name = 'google-login'

urlpatterns = [
    path("callback/", GoogleLoginApi.as_view(), name="callback-raw"),
    path("redirect/", GoogleLoginRedirectApi.as_view(), name="redirect-raw"),
]
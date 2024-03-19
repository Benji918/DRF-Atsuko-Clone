from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
import uuid
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    username = models.CharField(_('username'), unique=True, max_length=50, blank=False, null=False)
    email = models.EmailField(_('email address'), unique=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.email
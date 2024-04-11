from django.db.models.query import QuerySet

from .filters import CustomUserFilter
from .models import CustomUser


def user_get_login_data(*, user: CustomUser):
    return {
        "id": user.id,
        "email": user.email,
        "is_active": user.is_active,
        "is_admin": user.is_admin,
        "is_superuser": user.is_superuser,
    }


def user_list(*, filters=None) -> QuerySet[CustomUser]:
    filters = filters or {}

    qs = CustomUser.objects.all()

    return CustomUserFilter(filters, qs).qs
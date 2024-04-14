import django_filters
from core.models import Product


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category', lookup_expr='iexact')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    product_name = django_filters.CharFilter(field_name='product_name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['category', 'price__lte', 'price__gte', 'product_name']

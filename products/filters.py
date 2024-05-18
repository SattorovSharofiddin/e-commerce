from datetime import timedelta

from django.utils import timezone
from django_filters import rest_framework as filters

from .models import Product


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    featured = filters.BooleanFilter(field_name='featured')
    best_seller = filters.BooleanFilter(field_name='best_seller')
    shop_collection = filters.BooleanFilter(field_name='shop_collection')
    category = filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    new_arrivals = filters.BooleanFilter(method='filter_new_arrivals')
    discounted_price = filters.BooleanFilter(method='filter_discounted_price')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'featured', 'best_seller', 'shop_collection', 'category', 'new_arrivals',
                  'discounted_price']

    def filter_new_arrivals(self, queryset, name, value):
        if value:
            week_ago = timezone.now() - timedelta(days=7)
            return queryset.filter(created_at__gte=week_ago)
        return queryset

    def filter_discounted_price(self, queryset, name, value):
        if value:
            return queryset.filter(discount__isnull=False)
        return queryset

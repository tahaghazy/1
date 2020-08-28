import django_filters
from .models import Post


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['second_category','category']
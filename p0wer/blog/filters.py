import django_filters
from .models import Post


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['fourth_category','category','second_category','third_category']
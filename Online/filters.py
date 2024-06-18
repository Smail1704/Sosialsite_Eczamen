from django_filters.rest_framework import FilterSet
from .models import Follow


class FollowFilter(FilterSet):
    class Meta:
        model = Follow
        fields = ['hashtag']

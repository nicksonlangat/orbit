import django_filters
from .models import Organization, Tag, TagSelection

class BaseOrganizationFilter(django_filters.FilterSet):
    class Meta:
        model = Organization
        fields = ("id", "url")


class BaseTagFilter(django_filters.FilterSet):
    class Meta:
        model = Tag
        fields = ("id", "name")

class BaseTagSelectionFilter(django_filters.FilterSet):
    class Meta:
        model = TagSelection
        fields = ("id", "user")

import django_filters
from .models import Organization

class BaseOrganizationFilter(django_filters.FilterSet):
    class Meta:
        model = Organization
        fields = ("id", "url")

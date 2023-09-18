from django.db.models.query import QuerySet

from .filters import (
    BaseOrganizationFilter
)
from .models import Organization

def organization_list(*, user, filters=None) -> QuerySet[Organization]:
    filters = filters or {}

    qs = Organization.objects.filter(user=user)

    return BaseOrganizationFilter(filters, qs).qs

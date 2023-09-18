from django.db.models.query import QuerySet

from .filters import (
    BaseOrganizationFilter,
    BaseTagFilter,
    BaseTagSelectionFilter
)
from .models import Organization, Tag, TagSelection

def organization_list(*, user, filters=None) -> QuerySet[Organization]:
    filters = filters or {}

    qs = Organization.objects.filter(user=user)

    return BaseOrganizationFilter(filters, qs).qs


def tag_list(*, filters=None) -> QuerySet[Tag]:
    filters = filters or {}

    qs = Tag.objects.all()

    return BaseTagFilter(filters, qs).qs


def tag_selection_list(*, user, filters=None) -> QuerySet[TagSelection]:
    filters = filters or {}

    qs = TagSelection.objects.filter(user=user)

    return BaseTagSelectionFilter(filters, qs).qs

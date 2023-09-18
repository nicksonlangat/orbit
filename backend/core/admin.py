from django.contrib import admin
from .models import Organization, Tag, TagSelection
# Register your models here.

admin.site.register(Organization)
admin.site.register(Tag)
admin.site.register(TagSelection)
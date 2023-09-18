from rest_framework import serializers
from .models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    repo = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Organization
        fields = ["id", "url", "name", "repo"]
    
    def get_name(self, obj):
        return obj.url.strip().split('/')[3]

    def get_repo(self, obj):
        return obj.url.strip().split('/')[4]



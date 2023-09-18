from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Organization, Tag, TagSelection

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


class TagSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tag
            fields = [
                 "id", "name"
                ]


class TagSelectionSerializer(serializers.ModelSerializer):
        class Meta:
            model = TagSelection
            fields = [
                 "id", "user", "tags"
                ]
            
        def to_representation(self, instance):
            data = super(TagSelectionSerializer, self).to_representation(instance)
            data["tags"] = TagSerializer(instance.tags.all(), many=True).data
            return data

class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = [
                 "id", "username", "first_name",
                 "last_name", "is_superuser"
                ]

class UserSignupSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = fields = ["username", "password", "first_name", "last_name"]
            extra_kwargs = {"password": {"write_only": True}}

        def validate_password(self, value):
            validate_password(value)
            return value

        def create(self, validated_data):
            user = User(**validated_data)
            user.set_password(validated_data["password"])
            user.save()
            return user

class UserPasswordResetSerializer(serializers.Serializer):
        email = serializers.EmailField(required=True)
        
        class Meta:
            fields = [ "email" ]


class UserPasswordSerializer(serializers.Serializer):
        password = serializers.CharField(required=True)
        
        class Meta:
            fields = [ "password" ]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.http import Http404
from django.contrib.auth.models import User

from .service import organization_create, scrape_data, get_github_issues, tag_create, tag_selection_create, tag_selection_update
from .paginator import get_paginated_response, PageNumberPagination
from .serializers import OrganizationSerializer, TagSelectionSerializer, TagSerializer, UserSerializer, UserSignupSerializer
from .selectors import organization_list, tag_list, tag_selection_list
from .models import Organization, Tag, TagSelection

class ListQuestionsApi(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        
        tag = request.query_params.get('tag')
        if tag != "":
            questions = scrape_data(tag)
        else:
            questions = scrape_data('django')
        
        return Response({"data": questions})


class GithubIssuesApi(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        url = request.query_params.get('url')

        if url == "" or url is None:
            try:
                url = Organization.objects.filter(user=request.user).first().url
            except AttributeError:
                pass

        issues = get_github_issues(url)

        return Response({"data": issues})

class OrganizationApi(APIView):

    class Pagination(PageNumberPagination):
        page_size = 12

    permission_classes = [IsAuthenticated]
    serializer_class = OrganizationSerializer

    def get_object(self, pk):
        try:
            return Organization.objects.get(pk=pk)
        except Organization.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            request.data["user"] = request.user
            org = organization_create(request.data)
            return Response(data={"id": org.id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        organizations = organization_list(user=request.user, filters=request.query_params)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=organizations,
            request=request,
            view=self
        )
    
    def delete(self, request, pk, format=None):
        organization = self.get_object(pk)
        organization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagApi(APIView):

    class Pagination(PageNumberPagination):
        page_size = 20

    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer

    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            tag = tag_create(request.data)
            return Response(data={"id": tag.id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        tags = tag_list(filters=request.query_params)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=tags,
            request=request,
            view=self
        )
    
    def delete(self, request, pk, format=None):
        tag = self.get_object(pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagSelectionApi(APIView):

    class Pagination(PageNumberPagination):
        page_size = 20

    permission_classes = [IsAuthenticated]
    serializer_class = TagSelectionSerializer

    def get_object(self, pk):
        try:
            return TagSelection.objects.get(pk=pk)
        except TagSelection.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        request.data["user"] = request.user.id
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            tag_selection = tag_selection_create(request.user, request.data)
            return Response(data={"id": tag_selection.id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        tag_selections = tag_selection_list(user=request.user, filters=request.query_params)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=tag_selections,
            request=request,
            view=self
        )
    

    def put(self, request, pk, format=None):  
        request.data["user"] = request.user.id      
        selection = self.get_object(pk)
        serializer = TagSelectionSerializer(selection, data=request.data)
        if serializer.is_valid():
            tag_selection = tag_selection_update(selection.pk, request.data)
            return Response(data={"id": tag_selection.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk, format=None):
        tag_selection = self.get_object(pk)
        tag_selection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserSignupApi(APIView):

    authentication_classes = []
    permission_classes = []
    serializer_class = UserSignupSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class UsersMeApi(APIView):

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def get(self, request, format=None):
        user = UserSerializer(request.user).data

        return Response(user)

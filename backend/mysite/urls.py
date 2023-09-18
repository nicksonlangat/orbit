from django.contrib import admin
from django.urls import path
from core.views import ListQuestionsApi, GithubIssuesApi, OrganizationApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListQuestionsApi.as_view(), name='questions'),
    path('issues', GithubIssuesApi.as_view(), name='issues'),
    path('organizations', OrganizationApi.as_view(), name='organizations'),
    path('organizations/<uuid:pk>/', OrganizationApi.as_view(), name='organization')
]

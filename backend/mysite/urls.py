from django.contrib import admin
from django.urls import path
from core.views import (
    ListQuestionsApi, GithubIssuesApi, 
    OrganizationApi, UserSignupApi, UsersMeApi,
    TagApi, TagSelectionApi
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListQuestionsApi.as_view(), name='questions'),
    path('issues', GithubIssuesApi.as_view(), name='issues'),
    path('organizations', OrganizationApi.as_view(), name='organizations'),
    path('organizations/<uuid:pk>/', OrganizationApi.as_view(), name='organization'),
    path('signup', UserSignupApi.as_view(), name='signup'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/me', UsersMeApi.as_view(), name='users-me'),
    path('tags', TagApi.as_view(), name='tags'),
    path('tags/selections', TagSelectionApi.as_view(), name='tags-selections'),
    path('tags/selections/<uuid:pk>/', TagSelectionApi.as_view(), name='tags-selection'),
]

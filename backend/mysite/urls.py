from django.contrib import admin
from django.urls import path
from core.views import ListQuestionsApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListQuestionsApi.as_view(), name='questions')
]

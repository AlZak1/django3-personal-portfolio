from django.urls import path
from .api_views import ProjectListAPIView

urlpatterns = [
    path('projects', ProjectListAPIView.as_view(), name='projects')
]

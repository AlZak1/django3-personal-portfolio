from rest_framework.generics import ListAPIView
from .serializers import ProjectSerializer
from ..models import Project

class ProjectListAPIView(ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

from rest_framework.generics import ListAPIView
from .serializers import ProjectSerializer
from .models import Project

class ProjectList(ListAPIView):
    queryset = Project.objects.all().order_by('created_at')
    serializer_class = ProjectSerializer

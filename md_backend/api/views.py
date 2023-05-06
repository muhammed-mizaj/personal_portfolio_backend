from rest_framework.generics import ListAPIView
from .serializers import ProjectSerializer
from .models import Project

class ProjectList(ListAPIView):
    queryset = Project.objects.filter(is_visible=True).order_by('-priority')
    serializer_class = ProjectSerializer

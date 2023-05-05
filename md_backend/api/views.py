from rest_framework.generics import ListAPIView
from .serializers import ProjectSerializer
from .models import Projects

class ProjectList(ListAPIView):
    queryset = Projects.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

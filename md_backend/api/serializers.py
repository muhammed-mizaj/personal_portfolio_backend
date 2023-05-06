

from rest_framework.serializers import ModelSerializer
from .models import Project
class ProjectSerializer(ModelSerializer):
    class Meta:
        model=Project
        depth=2
        fields='__all__'
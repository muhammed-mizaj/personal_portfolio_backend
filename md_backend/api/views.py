import imp
from django.shortcuts import render
from .models import Projects
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProjectSerializer

# Create your views here.
@api_view(['GET'])
def getProjects(request):
    projects=Projects.objects.all().order_by('-created')
    serializer=ProjectSerializer(projects,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getProject(request,pk):
    project=Projects.objects.get(id=pk)
    serializer=ProjectSerializer(project,many=False)
    return Response(serializer.data)
@api_view(['DELETE'])
def deleteProject(request,pk):
    project=Projects.objects.get(id=pk)
    project.delete()
    return Response('project was deleted')
@api_view(['PUT'])
def updateProject(request,pk):
    data=request.data
    project=Projects.objects.get(id=pk)
    serializer=ProjectSerializer(instance=project,data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def createProject(request):
    data=request.data
    project=Projects.objects.create(
        name=data['name'],
        description=data['description'],
        view_link=data['view_link'],    
        sourcecodelink=data['sourcecodelink']
    )
    serializer=ProjectSerializer(project,many=False)
    return Response(serializer.data)
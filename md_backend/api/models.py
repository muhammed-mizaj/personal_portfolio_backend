
from django.db import models

class Stack(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to="stacks/")

    def __str__(self):
        return self.name


class Project(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(default='code.jpg',upload_to="projects/",null=True,blank=True)
    short_desc=models.CharField(max_length=500,null=True,blank=True)
    description=models.CharField(max_length=1000,null=True,blank=True)
    source_code_link=models.CharField(max_length=200,null=True,blank=True)
    view_link=models.CharField(max_length=200,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    priority = models.PositiveIntegerField(default=0,null=True)
    stacks = models.ManyToManyField(Stack,null=True,blank=True)
    is_visible = models.BooleanField(default=True,null=True,blank=True)


    def __str__(self):
        return self.name

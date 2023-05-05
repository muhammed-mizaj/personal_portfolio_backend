
from django.db import models

class Stack(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to="stacks/")


class Projects(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(default='code.jpg',null=True,blank=True)
    description=models.CharField(max_length=200)
    source_code_link=models.CharField(max_length=200,null=True,blank=True)
    view_link=models.CharField(max_length=200,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    stacks = models.ManyToManyField(Stack,null=True,blank=True)


    def __str__(self):
        return self.name

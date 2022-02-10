
from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Projects(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/',default='code.jpg',null=True)
    description=models.CharField(max_length=200)
    sourcecodelink=models.CharField(max_length=200,null=True,blank=True)
    view_link=models.CharField(max_length=200,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    stack1=models.CharField(max_length=200,null=True,blank=True)
    stack2=models.CharField(max_length=200,null=True,blank=True)
    stack3=models.CharField(max_length=200,null=True,blank=True)
    stack4=models.CharField(max_length=200,null=True,blank=True)


    def __str__(self):
        return self.name

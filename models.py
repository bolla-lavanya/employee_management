from django.db import models

# Create your models here.

class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=200)
    loc=models.CharField(max_length=100)
    def __str__(self):
        return str(self.deptno)
class Employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=200)
    salary=models.IntegerField()
    deptno=models.ForeignKey(Department,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',null=True)
    video=models.FileField(upload_to='videos/',null=True)
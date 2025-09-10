from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,Department
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK,HTTP_400_BAD_REQUEST
from .serializer import EmployeeSerializer,DeparmentSerializer
from rest_framework.decorators import api_view

# Create your views here.
def display(request):
    return HttpResponse('response')
def insertemployee(request):
    if request.method=='GET':
        return render(request,'employee_management/insert.html')
    if request.method=='POST':
        empno=int(request.POST['empno'])
        empname=request.POST['empname']
        salary=int(request.POST['salary'])
        deptno=int(request.POST['deptno'])
        dept=Department.objects.get(deptno=deptno)
        image=request.FILES.get('image')
        video=request.FILES.get('video')
        emp= Employee(empno=empno,empname=empname,salary=salary,deptno=dept,image=image,video=video)
        emp.save()
        return redirect('selectemployee')
    
def selectemployee(request):
    salary_start=request.GET.get('salary_start')
    salary_end=request.GET.get('salary_end')
    emp=Employee.objects.all()
    if salary_start and salary_end:
        emp=emp.filter(salary__gte=salary_start,salary__lte=salary_end)
    if salary_start:
        emp=emp.filter(salary__gte=salary_start)
    if salary_end:
        emp=emp.filter(salary__lte=salary_end)
    
    return render(request,'employee_management/select.html',{'employee':emp,'salary_start':salary_start,'salary_end':salary_end})
def updateemployee(request,eno):
    emp=Employee.objects.get(empno=eno)
    if request.method=='GET':
        return render(request,'employee_management/update.html',{'emp':emp})
    if request.method=='POST':
        emp.empno=int(request.POST['empno'])
        emp.empname=request.POST['empname']
        emp.salary=int(request.POST['salary'])
        deptno=int(request.POST['deptno'])
        emp.dept=Department.objects.get(deptno=deptno)
        if 'image' in request.FILES:
            emp.image=request.FILES['image']
        if 'video' in request.FILES:
            emp.video=request.FILES['video']
        emp.save()
        return redirect('selectemployee')
def deleteemployee(request,eno):
    emp=Employee.objects.get(empno=eno)
    if request.method=='GET':
        return render(request,'employee_management/delete.html',{'emp':emp})
    if request.method=='POST':
        emp.delete()
        return redirect('selectemployee')
@api_view(['GET','POST'])
def employee_details(request):
    if request.method=='GET':
        emp=Employee.objects.all()
        e_serializer=EmployeeSerializer(emp,many=True)
        return Response(e_serializer.data)
    if request.method=='POST':
        e_serializer=EmployeeSerializer(data=request.data)
        if e_serializer.is_valid():
            e_serializer.save()
            return Response(e_serializer.data,status=HTTP_201_CREATED)
        return Response(e_serializer.errors,status=HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','PATCH','DELETE'])
def emp_process(request,eno):
    if request.method=='GET':
        emp=Employee.objects.get(empno=eno)
        e_serializer=EmployeeSerializer(emp)
        return Response(e_serializer.data,status=HTTP_200_OK)
    if request.method=='PUT':
        emp=Employee.objects.get(empno=eno)
        e_serializer=EmployeeSerializer(emp,data=request.data)
        if e_serializer.is_valid():
            e_serializer.save()
            return Response(e_serializer.data,status=HTTP_200_OK)
        return Response(e_serializer.errors,status=HTTP_400_BAD_REQUEST)
    if request.method=='PATCH':
        emp=Employee.objects.get(empno=eno)
        e_serializer=EmployeeSerializer(emp,data=request.data,partial=True)
        if e_serializer.is_valid():
            e_serializer.save()
            return Response(e_serializer.data,status=HTTP_201_CREATED)
        return Response(e_serializer.errors,status=HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        emp=Employee.objects.get(empno=eno)
        emp.delete()
        return Response('deleted sucessfully')
from django.urls import path
from . import views

urlpatterns=[
    path('',views.display),
    path('insert/',views.insertemployee,name='insertemployee'),
    path('select/',views.selectemployee,name='selectemployee'),
    path('update/<int:eno>/',views.updateemployee,name='updateemployee'),
    path('delete/<int:eno>/',views.deleteemployee,name='deleteemployee'),
    path('api/',views.employee_details),
    path('details/<int:eno>/',views.emp_process),
]

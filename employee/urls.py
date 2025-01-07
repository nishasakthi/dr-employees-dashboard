from django.urls import path
from . import views

urlpatterns = [
   path('employees/', views.index, name='index'),
   path('employees-list/', views.employees_list, name='employees-list'),
   path('employee-detail/<int:pk>', views.employee_detail, name='employees-detail'),
]

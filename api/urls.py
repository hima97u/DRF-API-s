from django.urls import path
from . import views

urlpatterns = [
    path('students/' , views.students),
    path('students/<int:pk>' , views.studentsDetail),


    path('employees/' , views.Employees.as_view()),
    path('employees/<int:pk>/' , views.EmolyeesDetail.as_view()),
]
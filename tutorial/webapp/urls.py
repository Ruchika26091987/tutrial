from django.urls import path
from . import views

urlpatterns = [
       path('', views.employeeList.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path('registerstudent/', views.register_student, name='register_student'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('exp8/courselist/', views.course_list, name='exp8_course_list'),
    path('exp8/course/<str:c_id>/', views.course_detail, name='exp8_course_detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('courselist/', views.course_list, name='course_list'),
    path('course/<str:c_id>/', views.course_detail, name='course_detail'),
    path('registration/<str:c_id>/', views.registration, name='registration'),
]
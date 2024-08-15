from django.urls import path
from . import views

#handler404 = views.error_404

urlpatterns = [
    path('fruitslist/', views.fruitslist),
    path('studentslist/', views.studentslist),
]
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_page, name='search_page'),
    path('search/student/', views.search_student, name='search_student'),
]

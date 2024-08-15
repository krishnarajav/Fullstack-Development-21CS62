from django.urls import path
from . import views

urlpatterns = [ 
    path('currentdatetime/', views.current_datetime, name='current_datetime'),
    path('currentdatetimewithoffset/<int:offset>/', views.current_datetime_with_offset, name='current_datetime_with_offset'),
]
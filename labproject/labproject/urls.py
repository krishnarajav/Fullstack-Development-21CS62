"""
URL configuration for labproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('date_time_app.urls')),
    path('', include('exp5.urls')),
    path('', include('exp6.urls')),
    path('', include('exp7.urls')),
    path('', include('exp8.urls')),
    path('', include('exp9.urls')),
    path('', include('exp10.urls')),
    path('', include('exp11.urls')),
    path('', include('exp12.urls')),
    path('', include('exp13.urls')),
]

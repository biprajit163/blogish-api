from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogish.urls')),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]

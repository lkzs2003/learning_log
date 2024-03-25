from django.urls import path, include, re_path
from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    re_path('register/', views.register, name='register'),
]
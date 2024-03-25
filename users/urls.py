from django.urls import path, include, re_path

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    re_path('register/', views.register, name='register'),
    ]
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register_staff, name="register_staff")
]
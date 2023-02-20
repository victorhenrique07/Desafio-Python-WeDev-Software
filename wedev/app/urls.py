from django.urls import path, include
from app import views

urlpatterns = [
    path('<str:pk>/', views.updateuser),
    path('profile/', views.student_course),
    path('cursos/', views.teste)
]

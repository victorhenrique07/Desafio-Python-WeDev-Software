from django.urls import path

from app import views

urlpatterns = [
    path("user/profile/edit/<int:pk>/", views.updateuser),
    path("user/profile/<str:pk>/", views.viewprofile),
    path("users/alunos", views.viewalunos),
    path("cursos/", views.viewcursos)
]

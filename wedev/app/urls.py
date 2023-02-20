from app import views
from django.urls import path

urlpatterns = [
    path("user/edit/<str:pk>/", views.updateuser),
]

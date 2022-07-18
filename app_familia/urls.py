from django.contrib import admin
from django.urls import path
from app_familia import views

urlpatterns = [
    path('', views.inicio),
    path('yo', views.ver_yo),
    path('padre', views.ver_padre),
    path('madre', views.ver_madre),
    path('hermano', views.ver_hermano),
    
]

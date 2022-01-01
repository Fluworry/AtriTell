from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.note_create),
    path('<str:note_url>/', views.note_get)
]

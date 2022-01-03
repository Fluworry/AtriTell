from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.note_create),
    path('auth', views.account_auth),
    path('register', views.account_register),
    path('<str:note_url>/', views.note_get_or_save)
]

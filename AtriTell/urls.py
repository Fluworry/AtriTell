from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('note', views.note_create),
    path('auth', views.account_auth),
    path('register', views.account_register),
    path('logout/', views.account_logout),
    path('account', views.account_settings),
    path('<str:note_url>/', views.note_get_or_save)
]

from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.article_create),
    path('<str:article_url>/', views.article_get)
]

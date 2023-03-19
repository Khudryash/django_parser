from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('load/', views.load),
    path('<str:number>/', views.page, name="index")
]

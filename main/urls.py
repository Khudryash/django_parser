from django.urls import path
from . import views

urlpatterns = [
    path('load/', views.load),
    path('home/', views.home),
    path('<str:number>/', views.page, name="index")
]

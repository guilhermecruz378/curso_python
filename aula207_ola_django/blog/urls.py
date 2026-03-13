from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_blog),
    path('exemplo/', views.exemplo)
]

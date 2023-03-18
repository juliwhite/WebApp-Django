from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registerActivity/', views.registerActivity),
    path('deleteActivity/<activities>', views.deleteActivity)
]
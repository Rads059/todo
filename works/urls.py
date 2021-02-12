from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index, name="list"),
    path('update_works/<str:pk>/', views.updateWorks, name="update_works"),
    path('delete/<str:pk>/', views.deleteWorks, name="delete"),
]
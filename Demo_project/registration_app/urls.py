from django.urls import path
from django.urls import include
from .import views
urlpatterns = [
    path('', views.index),
    path('demo_app/', views.demo_call),
    path('success/', views.success_call),
    path('save_password/', views.save_pword),
    path('reset__user_password/', views.reset_password,name='reset')
]
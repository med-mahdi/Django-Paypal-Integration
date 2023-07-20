from django.urls import path , include
from . import views
from django.views.generic import View

urlpatterns = [
    path('', views.home, name='index'),
    path('payment-completed/', views.successful, name='payment-completed'),
    path('payment-failed/', views.cancelled, name='payment-failed'),
]
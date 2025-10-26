from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('django/', views.django_welcome, name='django_welcome'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('singup/', views.signup, name='SIGNUP'),
    path('login/', views.login, name='LOGIN'),
]
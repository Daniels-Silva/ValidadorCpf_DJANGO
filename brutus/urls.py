
from django.urls import path
from . import views

urlpatterns = [
    path('', views.validar_cpf, name='validar_cpf'),  
    path('validar_cpf/', views.validar_cpf, name='validar_cpf'),
    path('remove_caracteres_especiaiss/', views.remove_caracteres_especiaiss, name='remove_caracteres_especiaiss')

]


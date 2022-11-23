from django.urls import path
from .views import index, inscricoes, cadastro

urlpatterns = [
    path('', index, name='index'),
    path('form/inscricoes', inscricoes, name='form/inscricoes'),
    path('form/cadastrar', cadastro, name='form/cadastrar'),
]

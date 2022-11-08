from django.urls import path
from .views import index, curso_form

urlpatterns = [
    path('', index, name='index'),
    path('curso_form/', curso_form, name='curso_form'),
]

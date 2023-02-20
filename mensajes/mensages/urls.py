from django.urls import path
from .views import index, images, usuarios
urlpatterns = [
    path('', index, name='index'),
    path('images/', images, name='images'),
    path('usu/', usuarios, name='usuarios')
]

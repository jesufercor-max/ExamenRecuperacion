from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index , name='index'),
    path('ejercicio1/<str:animal_contiene>/<str:refugio_contiene>/', views.Ejercicio1, name='ejercicio1'),
    path('ejercicio2/<str:vacuna_fabricante>/<str:vacuna_nombre>/', views.Ejercicio2, name='ejercicio2'),
]
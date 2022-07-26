from django.contrib import admin
from django.urls import path
from MVT.views import agrega_familiar , lista_familiares

urlpatterns = [
        path('agrega-familiar/<tipo_f>/<nombre>/<apellido>/<edad>/<estado_f>/', agrega_familiar),
        path('lista-familiares/', lista_familiares),
]

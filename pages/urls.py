from django.urls import path
from .views import PaginaAbout, PaginaInicio

urlpatterns=[
    path('', PaginaInicio.as_view(), name='home'),
    path('about/', PaginaAbout.as_view(),name="about"),
   
    ]
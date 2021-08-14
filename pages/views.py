from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class PaginaInicio(TemplateView):
    template_name = 'home.html'
class PaginaAbout(TemplateView):
    template_name= 'about.html'





from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class HomepgView(TemplateView):
    template_name = 'home.html'

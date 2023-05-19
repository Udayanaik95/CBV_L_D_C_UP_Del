from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from django.http import HttpResponse
from app.models import *

# Create your views here.

class Home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'
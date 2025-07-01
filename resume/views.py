# news/views.py
from django.shortcuts import render
from .models import Skill, Portfolio

def home_view(request):
    skills = Skill.objects.all()
    portfolios = Portfolio.objects.all()
    return render(request, 'resume.html', {
        'skills': skills,
        'portfolios': portfolios,
    })

from django.shortcuts import render
from .models import skill


def index(request):
    skills = skill.objects.all()
    context = {
        'title': 'Skill',
        'skill': skills
    }
    return render(request, 'skill/index.html', context)

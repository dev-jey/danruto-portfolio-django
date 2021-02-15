from django.shortcuts import render
from .models import About, Skill, Project


def get_home(request):
    about = About.objects.all().first()
    return render(request, 'index.html', {"about": about})


def get_about(request):
    about = About.objects.all().first()
    skills = Skill.objects.all()
    return render(request, 'about.html', {"about": about, "skills": skills})


def get_portfolio(request):
    projects = Project.objects.filter(active=True)
    about = About.objects.all().first()
    # featured_project = projects.filter(featured=True).first()
    # clients = Client.objects.all()
    return render(request, 'reile.html', {"projects": projects, "about": about})

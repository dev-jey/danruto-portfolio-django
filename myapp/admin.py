from django.contrib import admin

from myapp.models import Project, About, Skill

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(About)

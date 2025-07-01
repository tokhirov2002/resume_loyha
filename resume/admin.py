# news/admin.py
from django.contrib import admin
from .models import Skill, Portfolio

admin.site.register(Skill)
admin.site.register(Portfolio)

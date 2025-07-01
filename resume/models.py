# news/models.py
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/')  # .png yoki .svg
    rating = models.PositiveSmallIntegerField(default=0)  # 0 dan 5 gacha yulduzcha

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
